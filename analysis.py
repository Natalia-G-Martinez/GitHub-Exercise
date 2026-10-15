import pandas as pd

df = pd.read_csv('./data/actors.csv') # TODO: write a path to your csv file
column = "Gross" # TODO: name of a numeric column in your csv

"""
def load_data(path):

"""


def clean_data(df):
    return df

def summarize(df, column):
    print("Rows:", len(df))
    print("Mean:", df[column].mean())
    print("Max:", df[column].max())
    print("Min:", df[column].min())


def main():
    #df = load_data(csv_path)
    #df = clean_data(df)
    summarize(df, column)


if __name__ == "__main__":
    main()