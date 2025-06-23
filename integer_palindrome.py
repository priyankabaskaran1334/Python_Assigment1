def is_palindrome(n):
   
    return str(n) == str(n)[::-1]


number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
