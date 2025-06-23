def find_first_and_second_largest(arr):
    
    first, second = float('-inf'), float('-inf')
    
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return first, second


arr = list(map(int, input("Enter numbers separated by space: ").split()))
first, second = find_first_and_second_largest(arr)

if first == float('-inf') or second == float('-inf'):
    print("There aren't enough distinct numbers.")
else:
    print(f"First largest: {first}, Second largest: {second}")
