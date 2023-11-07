from InteriorPoint import InteriorPoint
import numpy as np
from Simplex import Simplex
from input_parser import parse_file
from Function import Function


def main():
    from input_parser import parse_file

    from input_parser import parse_file, parse_test
    print("InteriorPoint")
    function, matrix, b, approximation, initial_solution = parse_file("inputs/input6.txt", initial_point=True)
    interior_point = InteriorPoint(function, matrix, b, initial_solution, approximation, True)

    print(interior_point)
    solution = interior_point.optimize()
    print(solution)
    print("\n")
    print("Simplex")
    simplex = Simplex(function, matrix, b, approximation, True)
    print(simplex)
    solution = simplex.optimise(print_iterations=False)
    print(solution)


if __name__ == "__main__":
    main()