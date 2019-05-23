from algorithms.tsp import config
import matplotlib.pyplot as plt

def draw_scatter():
    x = config.get_value("X_i")
    y = config.get_value("Y_i")
    plt.scatter(x, y, c="#438eb9", alpha=0.9)