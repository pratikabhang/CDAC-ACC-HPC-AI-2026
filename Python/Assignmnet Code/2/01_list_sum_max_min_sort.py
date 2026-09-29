print('by default')

list1 = [10, 20, 30, 45, 25, 50, 85, 75, 35, 64]

print('list:', list1)
print('sum of all elements:', sum(list1))
print('maximum element:', max(list1))
print('minimum element:', min(list1))

list1.sort()
print('ascending order:', list1)

print('\nby user')

list_user = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    list_user.append(element)

print('user list:', list_user)
print('sum of all elements:', sum(list_user))
print('maximum element:', max(list_user))
print('minimum element:', min(list_user))

list_user.sort()
print('ascending order:', list_user)
