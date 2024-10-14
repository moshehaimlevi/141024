# start

import random

list1: list[bool] = [random.choice([True, False]) for i in range(3)]

print('all true?', all(list1))  # SECTION B

print('any true?', any(list1))  # SECTION C

print('all false', not all(list1))  # SECTION D

print('one false at least', not any(list1))  # SECTION E

import random

list2: list[int] = [random.randint(-2,2) for _ in range(5)]  # SECTION F
print('5 randoms', list2)

print('not all zero', any(list2))        # SECTION G

print('any not zero', any(list2))         # SECTION H

print('all zeros', not any(list2))     # SECTION I

print('at least one zero', not all(list2))     # SECTION j

