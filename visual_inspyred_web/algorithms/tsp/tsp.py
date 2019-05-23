from inspyred.benchmarks import Benchmark
import copy
from inspyred import ec
from inspyred.ec import emo
from inspyred.ec import selectors
from inspyred import swarm
import itertools
import math
import random
from algorithms.tsp import config


class TSP(Benchmark):
    """Defines the Traveling Salesman benchmark problem.

    This class defines the Traveling Salesman problem: given a set of
    locations and their pairwise distances, find the shortest route that
    visits each location once and only once. This problem assumes that
    the ``weights`` parameter is an *n*-by-*n* list of pairwise
    distances among *n* locations. This problem is treated as a
    maximization problem, so fitness values are determined to be the
    reciprocal of the total path length.

    In the case of typical evolutionary computation, a candidate solution
    is represented as a permutation of the *n*-element list of the integers
    from 0 to *n*-1. In the case of ant colony optimization, a candidate
    solution is represented by a list of ``TrailComponent`` objects which
    have (source, destination) tuples as their elements and the reciprocal
    of the weight from source to destination as their values.

    If evolutionary computation is to be used, then the ``generator``
    function should be used to create candidates. If ant colony
    optimization is used, then the ``constructor`` function creates
    candidates. The ``evaluator`` function performs the evaluation for
    both types of candidates.

    Public Attributes:

    - *weights* -- the two-dimensional list of pairwise distances
    - *components* -- the set of ``TrailComponent`` objects constructed
      from the ``weights`` attribute, where the element is the (source,
      destination) tuple and the value is the reciprocal of its
      ``weights`` entry
    - *bias* -- the bias in selecting the component of maximum desirability
      when constructing a candidate solution for ant colony optimization
      (default 0.5)

    """

    def __init__(self, weights):
        Benchmark.__init__(self, len(weights))
        self.weights = weights
        self.components = [swarm.TrailComponent((i, j), value=(1 / weights[i][j])) for i, j in
                           itertools.permutations(range(len(weights)), 2)]
        self.bias = 0.5
        self.bounder = ec.DiscreteBounder([i for i in range(len(weights))])
        self.maximize = True
        self._use_ants = False

    def generator(self, random, args):
        """Return a candidate solution for an evolutionary computation."""
        locations = [i for i in range(len(self.weights))]
        random.shuffle(locations)
        return locations

    def constructor(self, random, args):
        """Return a candidate solution for an ant colony optimization."""
        self._use_ants = True
        candidate = []
        #print(self.weights)
        while len(candidate) < len(self.weights) - 1:
            # Find feasible components
            feasible_components = []
            if len(candidate) == 0:
                feasible_components = self.components
            elif len(candidate) == len(self.weights) - 1:
                first = candidate[0]
                last = candidate[-1]

                feasible_components = [c for c in self.components if
                                       c.element[0] == last.element[1] and c.element[1] == first.element[0]]
            else:
                last = candidate[-1]

                already_visited = [c.element[0] for c in candidate]
                already_visited.extend([c.element[1] for c in candidate])
                already_visited = set(already_visited)
                feasible_components = [c for c in self.components if
                                       c.element[0] == last.element[1] and c.element[1] not in already_visited]

            if len(feasible_components) == 0:
                candidate = []
            else:
                # Choose a feasible component
                if random.random() <= self.bias:
                    next_component = max(feasible_components)
                else:
                    next_component = \
                    selectors.fitness_proportionate_selection(random, feasible_components, {'num_selected': 1})[0]
                candidate.append(next_component)
        return candidate

    def evaluator(self, candidates, args):
        """Return the fitness values for the given candidates."""
        fitness = []
        if self._use_ants:
            for candidate in candidates:
                total = 0
                for c in candidate:
                    total += self.weights[c.element[0]][c.element[1]]
                last = (candidate[-1].element[1], candidate[0].element[0])
                total += self.weights[last[0]][last[1]]
                fitness.append(1 / total)
        else:
            for candidate in candidates:
                total = 0
                for src, dst in zip(candidate, candidate[1:] + [candidate[0]]):
                    total += self.weights[src][dst]
                fitness.append(1 / total)
        return fitness

