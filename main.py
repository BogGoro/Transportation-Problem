import pandas as pd
from tabulate import tabulate
import numpy as np

def north_west(S: list[int], C: list[list[int]], D: list[int]) -> list[int]:
    pass

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
        solution1 = north_west(S, C, D)
        solution2 = vogel(S, C, D)
        solution3 = russel(S, C, D)
        print("North-West method: ", solution1)
        print("Vogel's approximation method: ", solution2)
        print("Russell's approximation method: ", solution3)
    except Exception:
        print("The method is not applicable!")


if __name__ == "__main__":
    main()