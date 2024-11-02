# Simplex method for maximization

### Input:

• A vector of coefficients of supply - S. <br />
• A matrix of coefficients of costs - C. <br />
• A vector of coefficients of demand - D. <br />

### Output:

1. The string ”The method is not applicable!” <br />
   or <br />
2. The string ”The problem is not balanced!” <br />
   or <br />
3. Input parameter table. <br />
4. Matrix of initial basic feasible solution - x0 using North-West corner method, Vogel’s approximation method, and Russell’s approximation method.

## Tests:

### Input:

```
1 2 3
4 7 2 9
5 1 7 3
3 3 8 4
2 2 1 1

```

### Output:

```
+----------------------+-----+-----+-----+-----+----------+
| Source\Destination   |   0 |   1 |   2 |   3 |   Supply |
|----------------------+-----+-----+-----+-----+----------|
| 0                    |   4 |   7 |   2 |   9 |        1 |
| 1                    |   5 |   1 |   7 |   3 |        2 |
| 2                    |   3 |   3 |   8 |   4 |        3 |
| Demand               |   2 |   2 |   1 |   1 |        6 |
+----------------------+-----+-----+-----+-----+----------+
North-West method:  [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]
Vogel's approximation method:  [[0, 0, 1, 0], [0, 2, 0, 0], [2, 0, 0, 1]]
Russell's approximation method:  [[0, 0, 1, 0], [0, 2, 0, 0], [2, 0, 0, 1]]
```

### Input:

```
7 4 9
9 4 2 6
7 3 6 4
0 8 4 3
5 5 6 4

```

### Output:

```
+----------------------+-----+-----+-----+-----+----------+
| Source\Destination   |   0 |   1 |   2 |   3 |   Supply |
|----------------------+-----+-----+-----+-----+----------|
| 0                    |   9 |   4 |   2 |   6 |        7 |
| 1                    |   7 |   3 |   6 |   4 |        4 |
| 2                    |   0 |   8 |   4 |   3 |        9 |
| Demand               |   5 |   5 |   6 |   4 |       20 |
+----------------------+-----+-----+-----+-----+----------+
North-West method:  [[5, 2, 0, 0], [0, 3, 1, 0], [0, 0, 5, 4]]
Vogel's approximation method:  [[0, 1, 6, 0], [0, 4, 0, 0], [5, 0, 0, 4]]
Russell's approximation method:  [[0, 5, 2, 0], [0, 0, 4, 0], [5, 0, 0, 4]]
```

### Input:

```
6 2 5
10 54 77 12
38 54 23 43
48 17 36 29
3 3 4 3

```

### Output:

```
+----------------------+-----+-----+-----+-----+----------+
| Source\Destination   |   0 |   1 |   2 |   3 |   Supply |
|----------------------+-----+-----+-----+-----+----------|
| 0                    |  10 |  54 |  77 |  12 |        6 |
| 1                    |  38 |  54 |  23 |  43 |        2 |
| 2                    |  48 |  17 |  36 |  29 |        5 |
| Demand               |   3 |   3 |   4 |   3 |       13 |
+----------------------+-----+-----+-----+-----+----------+
North-West method:  [[3, 3, 0, 0], [0, 0, 2, 0], [0, 0, 2, 3]]
Vogel's approximation method:  [[3, 0, 0, 3], [0, 0, 2, 0], [0, 3, 2, 0]]
Russell's approximation method:  [[3, 0, 0, 3], [0, 0, 2, 0], [0, 3, 2, 0]]
```
