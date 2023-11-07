import argparse
import numpy
import warnings
from InteriorPoint import InteriorPoint
from Simplex import Simplex, InfeasibleSolution, AlternatingOptima
from input_parser import parse_file
numpy.seterr(all='warn')

warnings.filterwarnings("error", category=RuntimeWarning)


def print_interior_point_algorithm(interior_point: InteriorPoint):
    print(interior_point)
    try:
        solution = interior_point.optimize()
        print(solution)
    except Warning:
        print("SOLUTION:\nThe method is not applicable!")
    print("\n")


def main():
    print("InteriorPoint")
    function, matrix, b, approximation, initial_solution = parse_file("inputs/input7.txt", initial_point=True)
    print_interior_point_algorithm(
        InteriorPoint(function, matrix, b, initial_solution, approximation, True, 0.5)
    )
    print_interior_point_algorithm(
        InteriorPoint(function, matrix, b, initial_solution, approximation, True, 0.9)
    )
    print("Simplex")
    simplex = Simplex(function, matrix, b, approximation, True)
    print(simplex)
    try:
        solution = simplex.optimise(print_iterations=False)
        print(solution)
    except InfeasibleSolution:
        print("SOLUTION:\nThe method is not applicable!")
    except AlternatingOptima as e:
        print(e.solution)
        print("Alternating optima detected")


if __name__ == "__main__":
    main()
