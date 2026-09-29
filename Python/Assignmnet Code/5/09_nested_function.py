def outer():
    name = input("Enter your name: ")

    def inner():
        print("Hello", name)

    inner()

outer()
