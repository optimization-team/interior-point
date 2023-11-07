from dataclasses import dataclass

from Function import Function
import numpy as np

from Exceptions import (AlternatingOptima, InfeasibleSolution,
                        InvalidRightVector, DivergenceException)


@dataclass
class Solution:
    """
    Custom exception class for the Simplex algorithm. Contains solution for an optimization problem.

    Attributes
    ----------
    x: np.array
    opt: float
    """

    x: np.array
    opt: float

    def __str__(self):
        return (
            f"SOLUTION: \n"
            f"Vector of decision variables: ({', '.join(map(str, self.x))}),\n"
            f"Optimal value: {self.opt}"
        )


class InteriorPoint:
    """
        Interior point method implementation for calculating the optimal value of input vector for a given function and constraints.
        Attributes
        ----------
            Initial variables:
            ------------------
            function: Function

            constraints_matrix: np.array

            C: np.array
                function with slack variables

            A: np.array
                matrix of constraints (assumed that all given in the form of inequalities) with slack variables

            b: np.array
                right hand side column vector (size n x 1)

            eps: int
                approximation of an answer (number of digits after comma)

            m: int
                number of constraints

            n: int
                number of variables

            alpha: float
                distance that could be moved before the feasible region is left.
                0 < alpha < 1
    """

    def __init__(
            self,
            C: Function,
            A: np.array,
            b: np.array,
            initial_solution: np.array,
            eps: int = 2,
            to_maximize=True,
            alpha: float = 0.5
    ):
        self.to_maximize = to_maximize
        self.initial_solution = initial_solution
        self.function = C
        self.constraints_matrix = A
        self.C = np.hstack((np.array(C.coefficients), np.zeros(A.shape[0])))
        self.A = np.hstack((A, np.identity(A.shape[0])))
        self.b = b
        self.eps = eps
        self.epsilon = 1 / (10 ** eps)
        self.solution = np.array
        self.iteration = 0
        self.m, self.n = self.A.shape
        self.alfa = alpha
        self.check_inputs()

    def check_inputs(self):
        if not np.array_equal(np.array(np.dot(self.A, self.initial_solution)).flatten(), np.array(self.b)):
            raise DivergenceException(self.initial_solution)
        if any(map(lambda x: x < 0, self.b)):
            raise InvalidRightVector(self.b)

    def optimize(self):
        self.solution = self.initial_solution
        if not self.to_maximize:
            coefficients = list(map(lambda x: -x, self.C))
        else:
            coefficients = np.copy(self.C)
        accuracy = float('inf')
        while accuracy > self.epsilon:
            d = np.diag(self.solution)
            a_w = self.A @ d
            c_w = d @ coefficients
            p = np.identity(self.n) - np.transpose(a_w) @ np.linalg.inv(a_w @ np.transpose(a_w)) * a_w
            c_p = p @ c_w
            v = np.absolute(np.min(c_p))
            x_w = np.transpose(np.array([1.] * self.n) + self.alfa / v * c_p)
            next_solution = np.ndarray.tolist(np.transpose(d @ x_w))[0]
            accuracy = np.linalg.norm(np.subtract(self.solution, next_solution), ord=2)
            self.solution = next_solution

            if any(map(lambda x: x < 0, self.solution[:self.n - self.m])):
                raise DivergenceException(self.solution[:self.n - self.m])

        return Solution([round(i, self.eps) for i in self.solution[:self.n - self.m]],
                        round(self.function(self.solution[:self.n - self.m]), self.eps))

    def __str__(self):
        to_maximize = "max" if self.to_maximize else "min"
        constraints = f""
        for i in range(self.m):
            constraints += f"{self.constraints_matrix[i]} <= {self.b[i]}\n"
        constraints = constraints[:-1]
        constraints = constraints.replace("[[", "|").replace("]]", "|")
        approximation = f"Approximation: {self.eps}"
        alpha = f"Alpha: {self.alfa}"
        return f"LPP:\n{self.function} -> {to_maximize}\n{constraints}\n{approximation}\n{alpha}\n"


if __name__ == "__main__":
    from input_parser import parse_file, parse_test

    function, matrix, b, approximation, initial_solution = parse_file("inputs/input5.txt", initial_point=True)
    interior_point = InteriorPoint(function, matrix, b, initial_solution, approximation, True)

    print(interior_point)
    solution = interior_point.optimize()
    print(solution)
