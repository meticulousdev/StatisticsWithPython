import pandas as pd

from scipy import stats

if __name__ == "__main__":
    dataset = pd.read_csv("../testdata/dataset.csv")

    grouped = dataset.groupby('I1')

    # Kruskal-Wallis Test
    # H_value, p_value = stats.kruskal()

    print()