def iterator_example():
    text = input("Enter a word: ")

    it = iter(text)

    print(next(it))
    print(next(it))

iterator_example()
