print('by default')

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}

no_commons = set_a.symmetric_difference(set_b)

print('set a:', set_a)
print('set b:', set_b)
print('after removing common elements:', no_commons)