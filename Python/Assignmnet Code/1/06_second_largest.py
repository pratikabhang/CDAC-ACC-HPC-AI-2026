list1 = [45,25,50,85,75,85,100,92,61]
print('original list:',list1)

list2 = list(set(list1))
list2.sort()
print('no duplicate list:',list2)

second_large = list2[-2]
print("second largest no.:", second_large)
