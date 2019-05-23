import collections
import copy
import inspyred
import math
from algorithms.tsp import config
from algorithms.tsp import observers

class ACS(inspyred.ec.EvolutionaryComputation):
    """Represents an Ant Colony System discrete optimization algorithm.

    This class is built upon the ``EvolutionaryComputation`` class making
    use of an external archive. It assumes that candidate solutions are
    composed of instances of ``TrailComponent``.

    Public Attributes:

    - *components* -- the full set of discrete components for a given problem
    - *initial_pheromone* -- the initial pheromone on a trail (default 0)
    - *evaporation_rate* -- the rate of pheromone evaporation (default 0.1)
    - *learning_rate* -- the learning rate used in pheromone updates
      (default 0.1)

    """

    def __init__(self, random, components):
        inspyred.ec.EvolutionaryComputation.__init__(self, random)
        self.components = components
        self.evaporation_rate = 0.1
        self.initial_pheromone = 0
        self.learning_rate = 0.1
        self._variator = self._internal_variator
        self.archiver = self._internal_archiver
        self.replacer = inspyred.ec.replacers.generational_replacement
        self.observer = observers.stats_observer

    @property
    def variator(self):
        return self._variator

    @variator.setter
    def variator(self, value):
        self._variator = [self._internal_variator]
        if isinstance(value, collections.Sequence):
            self._variator.extend(value)
        else:
            self._variator.append(value)

    def _internal_variator(self, random, candidates, args):
        offspring = []
        for i in range(len(candidates)):
            offspring.append(self.generator(random, args))
        return offspring

    def _internal_archiver(self, random, population, archive, args):
        best = max(population)
        if len(archive) == 0:
            archive.append(best)
        else:
            arc_best = max(archive)
            if best > arc_best:
                archive.remove(arc_best)
                archive.append(best)
            else:
                best = arc_best
        for c in self.components:
            c.pheromone = ((1 - self.evaporation_rate) * c.pheromone +
                           self.evaporation_rate * self.initial_pheromone)
        for c in self.components:
            if c in best.candidate:
                c.pheromone = ((1 - self.learning_rate) * c.pheromone +
                               self.learning_rate * best.fitness)
        return archive
