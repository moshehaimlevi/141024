# START

# SECTION NUMBER 11:
total = 0

sentinel = 0
while True:
    number1 = int(input('enter a number:'))
    if number1 == sentinel:
        break
    if number1 < sentinel:
        total += number1
print(total)

# SECTION NUMBER 12:

list1 = []

count = 0

while count < 10:
    number2 = int(input('enter the number:'))
    list1.append(number2)
    count += 1
print(", ".join(str(list1[i]) for i in range(9, -1, -1)))

# SECTION NUMBER 13:

list_p = []

while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    for x in range(2, n + 1):
        is_prime = True
        if x > 2 and x % 2 == 0:
            is_prime = False
        else:
            divider = 3
            while divider * divider <= x:
                if x % divider == 0:
                    is_prime = False
                divider += 2
        if is_prime:
            list_p.append(x)
print(sorted(list_p))

# SECTION NUMBER 14:

list_of_5 = []

count = 0

while count < 5:
    number = float(input(f"Enter number {count + 1}: "))
    list_of_5.append(number)
    count += 1

average = sum(list_of_5) / 5

larger_numbers = [num for num in list_of_5 if num > average]

print(f"\n{average}")
print(f"{len(larger_numbers)}")
print(", ".join(str(num) for num in larger_numbers) if larger_numbers else "None")



# SECTION NUMBER 15:

first_n = int(input("Enter the 1st: "))
sec_n = int(input("Enter the 2nd number: "))

if sec_n == 0:
    print("Cannot divide by zero.")
else:
    result = first_n / sec_n
    print(f" {first_n} / {sec_n} is {result}.")

# END












































