my_tuple = (10, 20, 30, 40, 50)
search_for = 40

print('tuple:', my_tuple)
print('element:', search_for)

if search_for in my_tuple:
    position = my_tuple.index(search_for)
    print(f"The number {search_for} is at index position: {position}")
else:
    print(f"The number {search_for} is not in the tuple.")
