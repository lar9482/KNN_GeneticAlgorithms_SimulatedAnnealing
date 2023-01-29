from utils.ga_util import bitstr2float, real_to_binary, binary_to_real
from utils.ga_eval import sphere, griew, shekel, micha, langermann, odd_square, bump, _plot_f, _mesh, sphere_c, griew_c, langermann_c

from GA.genetic_algorithm import genetic_algorithm
from SA.simulated_annealing import simulated_annealing
from SA.schedule import linear_schedule, quadratic_schedule, trigonometric_schedule
import matplotlib.pyplot as plt

import numpy as np

def run_general_tests():
    _plot_f(sphere, *_mesh(-5, 5, -5, 5), title="The Sphere Function")
    _plot_f(griew, *_mesh(0, 200, 0, 200), title="Griewank's function")
    _plot_f(shekel, *_mesh(0, 10, 0, 10), title="Modified Shekel's Foxholes")
    _plot_f(micha, *_mesh(-10, 10, -10, 10), title="Michalewitz's function")
    _plot_f(langermann, *_mesh(0, 10, 0, 10), title="Langermann's function")
    _plot_f(odd_square, *_mesh(-5 * np.pi, 5 * np.pi, -5 * np.pi, 5 * np.pi), title="Odd Square Function")
    _plot_f(bump, *_mesh(0.1, 5, 0.1, 5), title="The Bump Function")

def run_genetic_algorithm_tests():
    fitness_function = sphere
    population_size = 30
    individual_size = 2
    crossover_rate = 1
    mutation_rate = 0.25
    min_value = -5
    max_value = 5
    maxProblem = False
    elitism_applied = True

    algo = genetic_algorithm(fitness_function, population_size, individual_size, crossover_rate, mutation_rate, min_value, max_value, maxProblem, elitism_applied)
    algo.run_algorithm(100)
    print()

def run_simulated_annealing_tests():
    value_function = griew
    constraint_function = griew_c
    min_value = 0
    max_value = 200
    dim = 2
    algo = simulated_annealing(value_function, constraint_function, min_value, max_value, dim)

    schedule = exponential_schedule
    # T_0 = 100000000
    T_0 = 1000
    T_Final = 0.01
    alpha = 0.8
    test1 = algo.run_algorithm(schedule, T_0, T_Final, alpha)

    print()

def plot_schedules():
    schedule = linear_schedule
    T_0 = 5000
    T_N = 0
    t = 1
    n = 20

    T = T_0
    x = []
    y = []

    while (True):
        if (T <= T_N):
            plt.plot(x, y)
            plt.xlabel('Time')
            plt.ylabel('Temperature')
            plt.show()
            print('done')
            break

        T = schedule(t, T_0, T_N, n)
        print(T)
        x.append(t)
        y.append(T)

        t += 1


def main():
    # run_general_tests()
    # run_genetic_algorithm_tests()
    # run_simulated_annealing_tests()
    # print(sphere(np.array([-4.829634895399511, -4.924000288382416])))
    plot_schedules()

if __name__ == "__main__":
    main()