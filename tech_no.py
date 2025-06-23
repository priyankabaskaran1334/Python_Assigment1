def is_tech_number(num):
    num_str = str(num)
    half = len(num_str) // 2
    first = int(num_str[:half])
    second = int(num_str[half:])
    total = first + second
    return total * total == num

number = int(input("Enter a number: "))
if is_tech_number(number):
    print("Tech Number")
else:
    print("Not a Tech Number")
