"""
Tests can be run with command: pytest
Test cases are located in "tests" folder.
"""
import os
import pytest
from numpy import matrix, array
from InteriorPoint import InteriorPoint, Solution
from Function import Function
from input_parser import parse_test


class InteriorPointTestCase:
    """
    Class for storing test cases

    Attributes
    ----------
    interior_point: InteriorPoint
        InteriorPoint-method object

    correct_solution: Solution
        an object with attributes:
            x: np.array
            opt: float
    """

    def __init__(
            self,
            function: Function,
            matrix: matrix,
            b: array,
            approximation: int | float,
            x: list[int],
            opt: int|float
    ):
        self.interior_point = InteriorPoint(function, matrix, array(b), approximation)
        self.correct_solution = Solution(array(x), float(opt))
        self.approximation = approximation

    def __str__(self):
        return (
            f"TestCase:\n{self.interior_point.C},\n"
            f"A:\n{self.interior_point.A},\n"
            f"b: {self.interior_point.b},\n"
            f"accuracy: {self.approximation},\n"
            +str(self.correct_solution)
        )


class TestInteriorPoint:
    """
    Class for testing InteriorPoint class

    Attributes
    ----------
    tests: list[str]
        list of test files
    test_cases: list[str]
        list of test cases

    Methods
    ----------
    test_interior_point(test_file)
        testing interior_point method on a test case with parametrization on list of test cases
    """

    tests = os.listdir("tests")
    test_cases = [os.path.join("tests", file) for file in tests]

    @pytest.mark.parametrize("test_file", test_cases)
    def test_simplex(self, test_file: str) -> None:
        """
        Parameters
        ----------
        test_file : str
            path to test file
        """

        testcase = InteriorPointTestCase(*parse_test(test_file))
        solution = testcase.interior_point.optimize()

        for i, val in enumerate(solution.x):
            assert round(val, testcase.approximation) == round(
                testcase.correct_solution.x[i], testcase.approximation
            )

        assert solution.opt == testcase.correct_solution.opt
