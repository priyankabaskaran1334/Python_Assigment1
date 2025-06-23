from itertools import permutations
num_str = input("Enter a number: ")
unique_perms = set(permutations(num_str))
for perm in sorted(unique_perms):
    print(''.join(perm))
