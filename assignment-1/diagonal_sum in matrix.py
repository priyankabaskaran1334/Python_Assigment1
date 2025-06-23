n = int(input("Enter matrix size: "))
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    print("Sum of row", i, "=", sum(matrix[i]))
for j in range(n):
    col_sum = 0
    for i in range(n):
        col_sum += matrix[i][j]
    print("Sum of column", j, "=", col_sum)
primary = 0
secondary = 0
for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n - 1 - i]

print("Sum of primary diagonal =", primary)
print("Sum of secondary diagonal =", secondary)
