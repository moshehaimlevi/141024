# start

# SECTION        IF:

# SECTION NUMBER 1:
num1: float = float(input('enter your number:'))

sentinel = 10


if num1 > sentinel:
    print(f"the number is bigger than 10: {10 - num1}")
else:
    print(f"The number is lower than 10: {num1 * 10}")

# SECTION NUMBER 2:

number1 = float(input('enter the 1st number:'))
number2 = float(input('enter the 2nd number:'))
number3 = float(input('enter the 3rd number:'))

ovr_num = number1 + number2 + number3

if ovr_num > 100:
    print(ovr_num)
else:
    print('the overall is NOT bigger than 100')


# SECTION NUMBER 4:


age: int = int(input('enter your age:'))

if 0 < age < 120:
    print(f"the age {age} and it is valid")
else:
    print('invalid age')

# SECTION NUMBER 5:

num3: int = int(input('enter a three digit number:'))

if 100 <= num3 <= 999:
    middle_digit =  str(num3)[1]
    print('the middle digit is', middle_digit)
else:
    print('try again')


#      END






















































