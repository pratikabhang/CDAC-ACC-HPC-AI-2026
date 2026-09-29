def calculate(a, b):
    return a + b, a - b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_value, difference = calculate(a, b)

print("Sum:", sum_value)
print("Difference:", difference)
