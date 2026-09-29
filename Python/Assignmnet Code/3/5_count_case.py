def count_case(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        else:
            pass

    print("Uppercase:", upper)
    print("Lowercase:", lower)


text = input("Enter text: ")
count_case(text)