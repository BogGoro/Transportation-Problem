import pandas as pd
from tabulate import tabulate
import numpy as np

def north_west(S: list[int], C: list[list[int]], D: list[int]) -> list[list[int]]:
    i, j = 0, 0
    allocation = np.zeros((len(S), len(D)))
    while i < len(S) and j < len(D):
        amount = min(S[i], D[j])
        allocation[i, j] = amount
        S[i] -= amount
        D[j] -= amount

        if S[i] == 0:
            i += 1
        if D[j] == 0:
            j += 1

    return allocation


def vogel(S: list[int], C: list[list[int]], D: list[int]) -> list[int]:
    pass

def russel(S: list[int], C: list[list[int]], D: list[int]) -> list[int]:
    pass


def main():
    try:
        S = list(map(int, input().split()))
        C = [list(map(int, input().split())) for _ in range(len(S))]
        D = list(map(int, input().split()))
        table = pd.DataFrame(C)
        table["Supply"] = S
        table.loc["Demand"] = D + [sum(D)]
        table.index.name = 'B\\A'
        if (sum(S) != sum(D)):
            print("The problem is not balanced!")
            return
        print(tabulate(table, headers = 'keys', tablefmt = 'psql'))
        solution1 = north_west(S.copy(), C, D.copy())
        solution2 = vogel(S.copy(), C, D.copy())
        solution3 = russel(S.copy(), C, D.copy())
        print("North-West method: ", solution1)
        print("Vogel's approximation method: ", solution2)
        print("Russell's approximation method: ", solution3)
    except Exception:
        print("The method is not applicable!")


if __name__ == "__main__":
    main()