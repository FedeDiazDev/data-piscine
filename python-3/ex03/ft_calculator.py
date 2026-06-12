class calculator:
	def __init__(self, vector: list[float]):
		assert isinstance(vector, list), "vector must be a list"
		assert all(isinstance(x, (int, float)) for x in vector), "vector must contain only numbers"
		self.vector = [float(x) for x in vector]

	def _apply(self, object, operator):
		assert isinstance(object, (int, float)), "operand must be a number"
		scalar = float(object)

		result = [operator(value, scalar) for value in self.vector]
		print(result)
		return None

	def __add__(self, object) -> None:
		return self._apply(object, lambda value, scalar: value + scalar)

	def __mul__(self, object) -> None:
		return self._apply(object, lambda value, scalar: value * scalar)

	def __sub__(self, object) -> None:
		return self._apply(object, lambda value, scalar: value - scalar)

	def __truediv__(self, object) -> None:
		assert object != 0, "division by zero"
		return self._apply(object, lambda value, scalar: value / scalar)
