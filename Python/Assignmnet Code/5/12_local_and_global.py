number = 10

def show_local():
    number = 20
    print("Local number:", number)

def show_global():
    global number
    number = 30
    print("Global number:", number)

show_local()
print("Outside function:", number)

show_global()
print("Outside function:", number)
