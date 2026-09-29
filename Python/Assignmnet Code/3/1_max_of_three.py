def max_of_three(a=45, b=99, c=100):
    return max(a, b, c)

print("Maximum using default values:", max_of_three())

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum using user values:", max_of_three(a, b, c))