import os
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Loads a CSV dataset, prints its dimensions, and returns it as a DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset, or None if an error occurs.
    """
    try:
        assert os.path.exists(path), f"The file '{path}' does not exist."
        assert path.lower().endswith(".csv"), "Invalid file format. Only .csv files are allowed."
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return None
    except Exception as error:
        print(f"Error: An error occurred while parsing the file: {error}")
        return None