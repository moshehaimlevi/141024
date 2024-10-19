# LOOPS

# SECTION NUMBER 6:

n = int(input('enter your number:'))

for x in range(0, n + 1):
    if x >= 1:
            print(x, end=' ')
print ()


# SECTION NUMBER 7:

first_num = int(input('enter the 1st number:'))
second_num = int(input('enter the 2nd number:'))

if first_num > second_num:
    first_num, second_num = second_num, first_num
    print(", ".join(str(x) for x in range (first_num, second_num + 1) if x % 2 == 0))
print ()


# SECTION NUMBER 8:


n2 = int(input('enter your number:'))

for x in range(0, n2 + 1):
    if x % 3 == 0 or x % 5 == 0:
        print(x, end=' ')
print()

# SECTION NUMBER 9:

n3 = int(input('enter your number:'))

for x in range(0, n3 + 1):
    if x % 7 == 0:
        print(x, end= ' ')
print()


# END








































































