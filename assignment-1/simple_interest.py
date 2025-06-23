def simple_interest(p, t, is_senior, is_other):
    if is_senior:
        r = 15
    elif is_other:
        r = 12
    else:
        r = 10
    return (p * r * t) / 100

p = float(input("Principal: "))
t = float(input("Time (years): "))
senior = input("Senior citizen? (yes/no): ").lower() == 'yes'
other = input("Other customer? (yes/no): ").lower() == 'yes'

interest = simple_interest(p, t, senior, other)
print("Simple Interest:", interest)
