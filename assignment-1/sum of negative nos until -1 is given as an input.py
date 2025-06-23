total = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    if num < 0:
        total += num

print("Sum of negative numbers entered:", total)
