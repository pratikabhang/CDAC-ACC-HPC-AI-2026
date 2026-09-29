def set_operations(first, second):
    a = set(first)
    b = set(second)

    common = a & b

    union = a | b
    only_first = a - b
    only_second = b - a

    even = []
    odd = []

    for number in common:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return a, b, union, common, only_first, only_second, even, odd


def main():
    n1 = int(input("Enter number of elements in first list: "))
    first = []

    for i in range(n1):
        number = int(input("Enter element: "))
        first.append(number)

    n2 = int(input("Enter number of elements in second list: "))
    second = []

    for i in range(n2):
        number = int(input("Enter element: "))
        second.append(number)

    unique_first, unique_second, union, common, only_first, only_second, even, odd = set_operations(first, second)

    print("Unique elements from first list:", unique_first)
    print("Unique elements from second list:", unique_second)
    print("Union:", union)
    print("Intersection:", common)
    print("Elements only in first list:", only_first)
    print("Elements only in second list:", only_second)
    print("Common even numbers:", even)
    print("Common odd numbers:", odd)


main()