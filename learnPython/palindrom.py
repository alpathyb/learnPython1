# create a funtion to solve Palindrome problem
def solve_palindrome(x):
    if not bool(x):
        return False

    x_str = str(x)
    if x_str == x_str[::-1]:
        return print(f"this data {x} is a palindrome")
    else:
        return print(f"this data {x} is not a palindrome")


# Testing your function here
test = [121, -121, "roor", "fajar"]

for i in range(len(test)):
    solve_palindrome(test[i])
