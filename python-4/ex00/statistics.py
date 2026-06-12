from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculates mean, median, quartiles, variance, and std dev from scratch

    using *args and executing requested operations in **kwargs.
    """
    data = list(args)
    n = len(data)
    operations = ["mean", "median", "quartile", "std", "var"]

    for key, value in kwargs.items():
        if value not in operations:
            continue
        if n == 0:
            print(f"ERROR")
            continue

        if value == "mean":
            mean = sum(data) / n
            print(f"Mean: {mean}")

        elif value == "median":
            sorted_data = sorted(data)
            mid = n // 2
            median = (sorted_data[mid] + sorted_data[-mid - 1]) / 2
            print(f"Median: {median}")

        elif value == "quartile":
            sorted_data = sorted(data)
            q1 = sorted_data[n // 4]
            q3 = sorted_data[3 * n // 4]
            print(f"quartile: [{q1}, {q3}]")

        elif value == "std":
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            std_dev = variance ** 0.5
            print(f"std: {std_dev}")

        elif value == "var":
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            print(f"var: {variance}")
    return  