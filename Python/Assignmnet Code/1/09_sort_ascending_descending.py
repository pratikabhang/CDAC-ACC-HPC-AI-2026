list=[]

print('by default')

list1 = [5,10,15,20,25]

print('original list:', list1)

list1.sort()

print('ascending order:',list1[::1])
print('descending order:',list1[::-1])


print('\nby user')

list_user = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    list_user.append(element)

print('original list:', list_user)

list_user.sort()

print('ascending order:',list_user[::1])
print('descending order:',list_user[::-1])