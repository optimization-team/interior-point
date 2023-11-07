class AlternatingOptima(Exception):
    def __init__(self, solution):
        super().__init__("Alternating optima detected!")
        self.solution = solution

class InfeasibleSolution(Exception):
    def __init__(self):
        super().__init__("Infeasible solution, method is not applicable!")

class InvalidRightVector(Exception):
    def __init__(self):
        super().__init__("Invalid right vector, method is not applicable!")