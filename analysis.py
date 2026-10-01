import pandas as pd

csv_path = "" # TODO: write a path to your csv file
column = "" # TODO: name of a numeric column in your csv


def load_data(path):
    df = pd.read_csv(path)
    return df


def summarize(df, column):
    print("Rows:", len(df))
    print("Mean:", df[column].mean()
    print("Max:", df[column].max())
    print("Min:", df[column].mn())


def main():
    df = load_data(CSV_PATH)
    df = clean_data(dataframe)
    summarize(df, COLUMN)


main