class AlternatingOptima(Exception):
    def __init__(self, solution):
        super().__init__("Alternating optima detected!")
        self.solution = solution