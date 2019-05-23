from random import Random
from time import time
import math
import inspyred
from algorithms.tsp import tsp, acs, config
import matplotlib.pyplot as plt
from algorithms.tsp import utils

def main(id, prng=None, display=True):

    config.set_value("observer", {})

    if prng is None:
        prng = Random()
        prng.seed(time())

    points = [(110.0, 225.0), (161.0, 280.0), (325.0, 554.0), (490.0, 285.0),
              (157.0, 443.0), (283.0, 379.0), (397.0, 566.0), (306.0, 360.0),
              (343.0, 110.0), (552.0, 199.0)]
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    config.set_value("X_i", x)
    config.set_value("Y_i", y)
    config.set_value("filename", "static\\images\\tsp\\")
    config.set_value("file_id", 0)
    utils.draw_scatter()
    filename = config.get_value("filename")
    filename = filename+str(config.get_value("file_id"))+".png"
    plt.savefig("static\\images\\tsp\\1.png")

    plt.plot([100, 100], [0, 0])
    plt.savefig("static\\images\\tsp\\2.png")
    #plt.show()
    weights = [[0 for _ in range(len(points))] for _ in range(len(points))]

    for i, p in enumerate(points):
        for j, q in enumerate(points):
            weights[i][j] = math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

    problem = tsp.TSP(weights)
    ac = acs.ACS(prng, problem.components)
    ac.terminator = inspyred.ec.terminators.generation_termination
    final_pop = ac.evolve(generator=problem.constructor,
                          evaluator=problem.evaluator,
                          bounder=problem.bounder,
                          maximize=problem.maximize,
                          pop_size=int(config.get_value("populations")),
                          max_generations=int(config.get_value("iterations")))

    if display:
        best = max(ac.archive)
        config.set_value("Best_solution", 1 / best.fitness)
        print('Best Solution:')
        for b in best.candidate:
            print(points[b.element[0]])
        print(points[best.candidate[-1].element[1]])
        print('Distance: {0}'.format(1 / best.fitness))
    return ac


if __name__ == '__main__':
    main(display=True)
