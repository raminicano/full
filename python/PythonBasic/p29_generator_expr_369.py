#!/usr/bin/env python
# to solve 369

numbers = (i for i in range(1,101))

data = list(numbers)

item = [3, 6, 9]

for i in data:
    if (i % 10 in item) or (i // 10 in item):
        print(' 👏', end=' ')
    else:
        print(f'{i:^5d}', end='')
    if (i % 10 in item) and (i // 10 in item):
        print('👏👏', end=' ')

    if i % 10 == 0:
        print('\n')