import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from typing import Any


def parse_population(value: Any) -> float:
    """Converts population strings like '34.5M' or '100k' into real numbers."""
    if pd.isna(value):
        return 0.0
    val_str = str(value).strip().upper()
    if val_str.endswith("M"):
        return float(val_str[:-1]) * 1_000_000
    if val_str.endswith("K"):
        return float(val_str[:-1]) * 1_000
    return float(val_str)


def display_population_comparison():
    """Loads population dataset, filters and cleans data for Spain vs France,

    and displays the comparison from 1800 to 2050.
    """
    try:
        path = "population_total.csv"
        df = load(path)
        if df is None:
            return
        my_country = "Spain"
        other_country = "France"
        data_my_country = df[df["country"] == my_country]
        data_other_country = df[df["country"] == other_country]
        assert (
            not data_my_country.empty
        ), f"Country '{my_country}' not found."
        assert (
            not data_other_country.empty
        ), f"Country '{other_country}' not found."

        years = [str(year) for year in range(1800, 2051)]

        pop_my_country = data_my_country[years].values[0]
        pop_other_country = data_other_country[years].values[0]

        y_my_country = [parse_population(v) for v in pop_my_country]
        y_other_country = [parse_population(v) for v in pop_other_country]

        x_years = [int(y) for y in years]

        plt.plot(x_years, y_my_country, label=my_country, color="blue")
        plt.plot(x_years, y_other_country, label=other_country, color="green")

        plt.title("Population Projections Comparison")
        plt.xlabel("Year")
        plt.ylabel("Population")

        def format_y_ticks(value, tick_number):
            return f"{int(value / 1_000_000)}M"

        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_y_ticks))

        plt.xticks(range(1800, 2051, 40))

        plt.legend(loc="lower right")

        plt.savefig("population_comparison.png", bbox_inches="tight")
        print("Success: Graph saved as 'population_comparison.png'")
        plt.close()

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    display_population_comparison()