try:
    A = float(input("Enter number A: "))
    B = float(input("Enter number B: "))

    result = A / B

    print("Result =", result)

except ValueError:
    print("Error: Please enter numeric values only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")