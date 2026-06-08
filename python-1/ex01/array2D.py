import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list), "famil must be a list"
        assert isinstance(start, int), "start must be an int"
        assert isinstance(end, int), "end must be an int"
        old_arr = np.array(family)
        print(f"My shape is: {old_arr.shape}")
        new_arr = old_arr[start:end]
        print(f"My shape is: {new_arr.shape}")
        new_list = new_arr.tolist()
        return new_list
    except AssertionError as error:
        print(f"AssertionError: {error}")
