import math

n = int(input("Enter the number of terms: "))
total = 0

for i in range(1, n+1):
    total += math.factorial(i) // i

print("Sum of the series is:", total)
