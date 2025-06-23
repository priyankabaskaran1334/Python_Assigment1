def is_perfect_number(n):
    return sum(i for i in range(1, n) if n % i == 0) == n


number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
