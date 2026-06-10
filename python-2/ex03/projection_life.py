import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_income(value) -> float:
    """Converts income strings like '1.2k' or '4.5M' into real numbers."""
    if pd.isna(value):
        return 0.0
    val_str = str(value).strip().upper()
    if val_str.endswith("M"):
        return float(val_str[:-1]) * 1_000_000
    if val_str.endswith("K"):
        return float(val_str[:-1]) * 1_000
    return float(val_str)


def display_projection_1900():
    """Loads income and life expectancy datasets, filters for the year 1900,"""
    try:
        file_income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        file_life = "life_expectancy_years.csv"

        df_income = load(file_income)
        df_life = load(file_life)

        if df_income is None or df_life is None:
            return

        income_1900 = df_income[["country", "1900"]].copy()
        life_1900 = df_life[["country", "1900"]].copy()

        income_1900["1900"] = income_1900["1900"].apply(parse_income)

        merged_df = pd.merge(
            income_1900, life_1900, on="country", suffixes=("_income", "_life")
        )

        x_gdp = merged_df["1900_income"]
        y_life = merged_df["1900_life"]

        plt.scatter(x_gdp, y_life, color="blue", alpha=0.7)

        plt.title("1900 Life Expectancy vs Gross National Product")
        plt.xlabel("Gross Domestic Product (GDP per capita)")
        plt.ylabel("Life Expectancy (years)")

        plt.xscale("log")

        plt.xticks(
            [300, 1000, 2000, 5000, 10000, 20000, 50000],
            ["300", "1k", "2k", "5k", "10k", "20k", "50k"],
        )

        plt.legend(loc="lower right")

        plt.savefig("projection_1900.png", bbox_inches="tight")
        print("Success: Graph saved as 'projection_1900.png'")
        plt.close()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    display_projection_1900()