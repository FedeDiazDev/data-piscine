def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    try:
        assert isinstance(height, list), "Height must be a list"
        assert isinstance(weight, list), "Weight must be a weight"
        assert len(height) == len(weight), "Lists must have the same length."
        assert all(isinstance(h, (int, float)) for h in height), "all heights\
            must be int or float"
        assert all(isinstance(w, (int, float)) for w in weight), "all weights\
            must be int or float"
        bmi_result = []
        for h, w in zip(height, weight):
            bmi_result.append(w / h**2)
        return bmi_result
    except AssertionError as error:
        print(f"AssertionError: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        assert isinstance(bmi, list), "bmi must be a list"
        assert all(isinstance(x, (int, float)) for x in bmi), "all bmi\
            values must be int or float"
        assert isinstance(limit, int), "all limits ustb be int"
        limit_result = []
        for b in bmi:
            limit_result.append(b > limit)
        return limit_result
    except AssertionError as error:
        print(f"AssertionError: {error} ")
