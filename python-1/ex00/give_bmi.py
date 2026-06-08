def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for a list of heights and weights.

    The function ensures both inputs are lists of identical length containing
    only integers or floats, then computes the BMI using the formula:
    weight / (height ** 2).

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list containing the calculated BMI values.
                           Returns an empty list if an assertion fails.
    """
    try:
        assert isinstance(height, list), "Height must be a list"
        assert isinstance(weight, list), "Weight must be a weight"
        assert len(height) == len(weight), "Lists must have the same length."
        assert all(isinstance(h, (int, float)) for h in height), \
            "all heights must be int or float"
        assert all(isinstance(w, (int, float)) for w in weight), \
            "all weights must be int or float"
        bmi_result = []
        for h, w in zip(height, weight):
            bmi_result.append(w / h**2)
        return bmi_result
    except AssertionError as error:
        print(f"AssertionError: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if BMI values exceed a given upper limit.

    The function validates that the BMI input is a list of numbers and the
    limit is an integer, then returns a list of booleans indicating whether
    each BMI value is strictly greater than the limit.

    Args:
        bmi (list[int | float]): A list of calculated BMI values.
        limit (int): The threshold value to compare against.

    Returns:
        list[bool]: A list of booleans where True means the\
            BMI exceeds the limit.
                    Returns None (or empty list) if an assertion fails.
    """
    try:
        assert isinstance(bmi, list), "bmi must be a list"
        assert all(isinstance(x, (int, float)) for x in bmi), \
            "all bmi values must be int or float"
        assert isinstance(limit, int), "all limits ustb be int"
        limit_result = []
        for b in bmi:
            limit_result.append(b > limit)
        return limit_result
    except AssertionError as error:
        print(f"AssertionError: {error} ")
