from typing import List

from scipy import stats
import scikit_posthocs as sp

if __name__ == "__main__":
    print("Kruskal Wallis Test")
    x: List[float] = [1, 2, 3, 4, 5]
    y: List[float] = [3, 4, 5, 6, 7, 8, 9]
    z: List[float] = [3, 4, 5, 6]

    H_value, p_value = stats.kruskal(x, y, z)
    print(f"statistic: {H_value}, p-value: {p_value}")

    arr = [x, y, z]
    p_value_posthoc: float = sp.posthoc_dunn(arr, p_adjust="holm")
    print(f"p-value (posthoc):")
    print(p_value_posthoc)
