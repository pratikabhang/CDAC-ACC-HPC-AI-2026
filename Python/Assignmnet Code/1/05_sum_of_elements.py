print('by default')

list1 = [45,25,50,85,75,85,100,92,61]

print('default list:', list1)
print('sum of all elements:', sum(list1))

print('\nby user')

list_user = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    list_user.append(element)

print('user list:', list_user)
print('sum of all elements:', sum(list_user))