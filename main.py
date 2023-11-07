import numpy
import warnings
from InteriorPoint import InteriorPoint
from Simplex import Simplex
from Exceptions import AlternatingOptima, InfeasibleSolution, InvalidRightVector, DivergenceException
from input_parser import parse_file

numpy.seterr(all='warn')
warnings.filterwarnings("error", category=RuntimeWarning)


def print_interior_point_algorithm(interior_point: InteriorPoint):
    print(interior_point)
    solution = interior_point.optimize()
    print(solution)


def main():
    print("InteriorPoint")
    function, matrix, b, approximation, initial_solution = parse_file("inputs/input5.txt", initial_point=True)
    try:
        print_interior_point_algorithm(
            InteriorPoint(function, matrix, b, initial_solution, approximation, True, 0.5)
        )
    except InvalidRightVector as e:
        print("The method is not applicable!")
        print(f"Invalid b vector: {e.vector}")
    except Warning or InfeasibleSolution:
        print("The problem does not have solution!")
    except AlternatingOptima as e:
        print(e.solution)
        print("Alternating optima detected")
    except DivergenceException as e:
        print("Method fall into divergent point.")
        print(f"Invalid initial point: {e.point}")
    except Exception as e:
        print(e)

    print("\n")

    try:
        print_interior_point_algorithm(
            InteriorPoint(function, matrix, b, initial_solution, approximation, True, 0.9)
        )
    except InvalidRightVector as e:
        print("The method is not applicable!")
        print(f"Invalid b vector: {e.vector}")
    except Warning or InfeasibleSolution:
        print("The problem does not have solution!")
    except AlternatingOptima as e:
        print(e.solution)
        print("Alternating optima detected")
    except DivergenceException as e:
        print("Method fall into divergent point.")
        print(f"Invalid initial point: {e.point}")
    except Exception as e:
        print(e)

    print("\n")

    print("Simplex")
    try:
        simplex = Simplex(function, matrix, b, approximation, True)
        print(simplex)
        solution = simplex.optimise(print_iterations=False)
        print(solution)
    except InvalidRightVector as e:
        print("The method is not applicable!")
        print(f"Invalid b vector: {e.vector}")
    except InfeasibleSolution:
        print("The problem does not have solution!")
    except AlternatingOptima as e:
        print(e.solution)
        print("Alternating optima detected")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
