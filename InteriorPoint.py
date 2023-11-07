from dataclasses import dataclass

from Function import Function
import numpy as np


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


class InteriorPoint:
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
        self.C = np.array(C.coefficients)
        self.A = A
        self.b = b
        self.eps = eps
        self.epsilon = 1 / (10 ** eps)
        self.solution = np.array
        self.iteration = 0
        self.m, self.n = self.A.shape
        self.alfa = alpha

    def build_initial_solution(self) -> np.array:
        pass

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
        return Solution([round(i, self.eps) for i in self.solution], round(self.function(self.solution), self.eps))

    def __str__(self):
        to_maximize = "max" if self.to_maximize else "min"
        constraints = f""
        for i in range(self.m):
            constraints += f"{self.constraints_matrix[i]} <= {self.b[i]}\n"
        constraints = constraints[:-1]
        constraints = constraints.replace("[[", "|").replace("]]", "|")
        approximation = f"Approximation: {self.eps}"
        return f"LPP:\n{self.function} -> {to_maximize}\n{constraints}\n{approximation}\n"


if __name__ == "__main__":
    function = Function([1, 1, 0, 0])
    constraints = np.matrix([[2, 4, 1, 0], [1, 3, 0, -1]])
    b = np.array([16.0, 9.0])
    initial_solution = np.array([1 / 2, 7 / 2, 1, 2])
    approximation = 3
    interior_point = InteriorPoint(function, constraints, b, initial_solution, approximation, True)
    print(interior_point)
    solution = interior_point.optimize()
    print(solution)
