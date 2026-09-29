list=[]

print('by default')

list_no = [1, 2, 3, 4, 5]
list_sq = []

for i in list_no:
    list_sq.append(i*i)

print('no of list:',list_no)
print('square no of list:',list_sq)


print('\nby user')

list_user = []
list_sq_user = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    list_user.append(element)

for i in list_user:
    list_sq_user.append(i*i)

print('no of list:',list_user)
print('square no of list:',list_sq_user)