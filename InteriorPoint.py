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
            eps: int = 2,
            to_maximize=True,
            alpha: float = 0.5
    ):
        self.to_maximize = to_maximize
        self.function = C
        self.constraints_matrix = A
        self.C = np.array(C.coefficients)
        self.A = A
        self.b = b
        self.eps = eps
        self.epsilon = 1 / (10 ** eps)
        self.iteration = 0
        self.m, self.n = self.A.shape
        self.alfa = alpha

        self.initial_solution = self.build_initial_solution()
        self.solution = self.initial_solution
        print(self.solution)

    def build_initial_solution(self) -> Solution:
        x = np.linalg.solve(self.A,self.b)
        return Solution(x,round(self.function(vector=x),self.eps))

    def optimize(self):
        if not self.to_maximize:
            coefficients = list(map(lambda x: -x, self.C))
        else:
            coefficients = np.copy(self.C)
        accuracy = float('inf')
        cur_x = self.solution.x
        while accuracy > self.epsilon:
            print('cur_x:',cur_x)
            d = np.diag(cur_x)
            a_w = self.A @ d
            c_w = d @ coefficients
            p = np.identity(self.n) - np.transpose(a_w) @ np.linalg.inv(a_w @ np.transpose(a_w)) * a_w
            c_p = p @ c_w
            v = np.absolute(np.min(c_p))
            x_w = np.transpose(np.array([1.] * self.n) + self.alfa / v * c_p)
            next_x = np.transpose(d @ x_w)
            accuracy = np.linalg.norm(np.subtract(cur_x, next_x), ord=2)
            cur_x = next_x
        self.solution = Solution(cur_x, round(self.function(cur_x), self.eps))
        return self.solution

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
    function = Function([5, 4])
    constraints = np.matrix([[1, 1], [0.75, 1]])
    b = np.array([20, 18])
    # initial_solution = np.array([1 / 2, 7 / 2, 1, 2])
    approximation = 1
    interior_point = InteriorPoint(function, constraints, b, approximation, True)
    print(interior_point)
    solution = interior_point.optimize()
    print(solution)
