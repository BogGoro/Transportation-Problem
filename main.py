import pandas as pd
from tabulate import tabulate
import numpy as np

def north_west(S: list[int], C: list[list[int]], D: list[int]) -> list[list[int]]:
    i, j = 0, 0
    allocation = [[0 for _ in range(len(D))] for _ in range(len(S))]
    while i < len(S) and j < len(D):
        # allocating
        amount = min(S[i], D[j])
        allocation[i][j] = amount
        S[i] -= amount
        D[j] -= amount

        # moving
        if S[i] == 0:
            i += 1
        if D[j] == 0:
            j += 1

    return allocation


def vogel(S: list[int], C: list[list[int]], D: list[int]) -> list[list[int]]:
    allocation = [[0 for _ in range(len(D))] for _ in range(len(S))]
    C_inf = max([max(row) for row in C]) + 1

    while sum(S) > 0 and sum(D) > 0:
        C_transpose = [[C[i][j] for i in range(len(S))] for j in range(len(D))]
        C_transpose_sorted = [sorted(C_transpose[i]) for i in range(len(D))]
        C_sorted = [sorted(C[i]) for i in range(len(S))]
        
        # calculating differences of two minimums in rows and columns
        min_diff_in_rows = [
            C_sorted[i][1] - C_sorted[i][0]
            if S[i] != 0 else -1
            for i in range(len(S))
        ]
        min_diff_in_columns = [
            C_transpose_sorted[i][1] - C_transpose_sorted[i][0]
            if D[i] != 0 else -1
            for i in range(len(D))
        ]
        diff_list = [min_diff_in_rows + [-1 for _ in range(len(D) - len(S))]]
        diff_list.append(min_diff_in_columns + [-1 for _ in range(len(S) - len(D))])
        diff_list = np.array(diff_list)

        i, j = np.unravel_index(np.argmax(diff_list), diff_list.shape)

        # fining the basic variable index
        basic_variable_arr = np.array([
            C_transpose[j][k] if S[k] != 0 else C_inf
            for k in range(len(S))
        ]) if i else np.array([
            C[j][k] if D[k] != 0 else C_inf
            for k in range(len(D))
        ])
        if i:
            i = np.unravel_index(np.argmin(basic_variable_arr), basic_variable_arr.shape)[0]
        else:
            i = j
            j = np.unravel_index(np.argmin(basic_variable_arr), basic_variable_arr.shape)[0]

        # allocating
        amount = min(S[i], D[j])
        allocation[i][j] = amount
        S[i] -= amount
        D[j] -= amount

        # replacing cells with demand = 0 or supply = 0 with pseudo infinity
        C = [
            [
                C[i][j] if D[j] != 0 and S[i] != 0 else C_inf
                for j in range(len(D))
            ]
            for i in range(len(S))
        ]

    return allocation

def russel(S: list[int], C: list[list[int]], D: list[int]) -> list[list[int]]:
    allocation = [[0 for _ in range(len(D))] for _ in range(len(S))]
    max_in_row = [max(row) for row in C]
    max_in_column = [max([C[i][j] for i in range(len(S))]) for j in range(len(D))]
    while sum(S) > 0 and sum(D) > 0:
        # table of differences with maximums, but if demand or supply is equal to 0 then it is 1
        table = np.array([
            [
                C[i][j] - max_in_row[i] - max_in_column[j]
                if D[j] > 0 and S[i] > 0 else 1
                for j in range(len(D))
            ]
            for i in range(len(S))
        ])

        # finding the minimum in the table
        i, j = np.unravel_index(np.argmin(table), table.shape)
        # allocating
        amount = min(S[i], D[j])
        allocation[i][j] = amount
        S[i] -= amount
        D[j] -= amount

    return allocation


def main():
    try:
        S = list(map(int, input().split()))
        C = [list(map(int, input().split())) for _ in range(len(S))]
        D = list(map(int, input().split()))
        table = pd.DataFrame(C)
        table["Supply"] = S
        table.loc["Demand"] = D + [sum(D)]
        table.index.name = 'Source\\Destination'
        if (sum(S) != sum(D)):
            print("The problem is not balanced!")
            return
        solution1 = north_west(S.copy(), C, D.copy())
        solution2 = vogel(S.copy(), C.copy(), D.copy())
        solution3 = russel(S.copy(), C, D.copy())
        print(tabulate(table, headers = 'keys', tablefmt = 'psql'))
        print("North-West corner method: ", solution1)
        print("Vogel's approximation method: ", solution2)
        print("Russell's approximation method: ", solution3)
    except Exception:
        print("The method is not applicable!")


if __name__ == "__main__":
    main()