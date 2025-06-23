import math

n = int(input("Enter number of terms: "))
total = 0

for i in range(1, n+1):
    s = i * (i + 1) // 2
    total += math.factorial(s)

print("Sum is:", total)
