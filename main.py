from InteriorPoint import InteriorPoint
import numpy as np
from Simplex import Simplex
from input_parser import parse_file
from Function import Function


def main():

    print("InteriorPoint")
    function, matrix, b, approximation, initial_solution = parse_file("inputs/input7.txt", initial_point=True)
    interior_point = InteriorPoint(function, matrix, b, initial_solution, approximation, True)
    np.set_printoptions(precision=approximation)

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