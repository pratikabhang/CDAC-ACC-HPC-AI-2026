print('by default')

list1 = [1, 25, 50, 75, 100]

print('default list:', list1)
print('largest element:', max(list1))

print('\nby user')

list_user = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    list_user.append(element)

print('user list:', list_user)
print('largest element:', max(list_user))