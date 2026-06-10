import matplotlib.pyplot as plt
from load_csv import load


def display_campus_life():
    """Loads life expectancy dataset and displays the data for Spain (Madrid campus)."""
    try:
        path = "life_expectancy_years.csv"
        df = load(path)
        if df is None:
            return
        spain_data = df[df["country"] == "Spain"]

        assert not spain_data.empty, "Country 'Spain' not found in the dataset."
        years = df.columns[1:]
        life_expectancy = spain_data.values[0][1:]
        plt.plot(years, life_expectancy, label="Spain")
        plt.title("Spain Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")

        plt.xticks(years[::40])

        plt.savefig("spain_life.png", bbox_inches="tight")
        print("Graph successfully saved as 'spain_life.png'")
        plt.close()

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    display_campus_life()