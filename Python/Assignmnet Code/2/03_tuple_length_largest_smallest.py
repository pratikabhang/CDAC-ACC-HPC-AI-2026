print('by default')

tuple1 = (1, 2, 3, 4, 5)

print('tuple:', tuple1)
print('length:', len(tuple1))
print('largest element:', max(tuple1))
print('smallest element:', min(tuple1))

print('\nby user')

list_user = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    list_user.append(element)

tuple_user = tuple(list_user)

print('tuple:', tuple_user)
print('length:', len(tuple_user))
print('largest element:', max(tuple_user))
print('smallest element:', min(tuple_user))
