number_1 = int(input("Write a number from 1 - 100: "))
number_2 = int(input("write another number from 1 - 100: "))

product = number_1 * number_2

if(product < 1000):
    print(f"The result is: {product}")
    
else:
    print(f"The result is: {number_1 + number_2}")

print("-------------------------------------------------")

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1,11):
    sum = previous_num + i
    print(f"Current number: {i}, Previous number: {previous_num}, sum: {sum}")
    previous_num = i

print("------------------------------------------------")

word = input("Write a word: ")
print(f"Orginal String is {word}")
print("Printing only even index chars")
size = len(word)

for i in range(0, size-1, 2):
    print(f"index[{i}]", word[i])

print('------------------------------------------------')

def remove_chars(word, num):
    print(f"Original string {word}")
    x = word[num:]
    return x
    
print("removing characters from a string")
print(remove_chars("name", 2))

print('--------------------------------------------------')

def first_last_same(numberlist):

    print(f"Given List: {numberlist}")
    first_value = numberlist[0]
    last_value = numberlist[len(numberlist)-1]

    if  first_value == last_value:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("Result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Result is", first_last_same(numbers_y))

print("----------------------------------------------------")

numberlist= [10, 20, 33, 46, 55]

print(f"Given numbers: {numberlist}")
print("Divisible by 5:")
for num in numberlist:
    if num % 5 == 0:
        print(num)

print("------------------------------------------------------")

string = "Emma is good developer. Emma is a writer"

count = string.count("Emma")

print(f"Emma appeared {count} times")

print("--------------------------------------------------------")

rows = 5

for r in range(1, rows + 1):
    for c in range(1, r + 1):
        print(c, end=" ")
    print(" ")

print("-----------------------------------------------------------")

for num in range(1,6):
    for i in range(num):
        print(num, end=" ")
    print(" ")

print("-----------------------------------------------------------")

number = int(input("write a number: "))
palindrome = "No"
original_number = number

reverse_number = 0
while number > 0:
    reminder = number % 10
    reverse_number = (reverse_number * 10) + reminder
    number = number // 10


if original_number == reverse_number:
    palindrome = "Yes"
    print(f"{palindrome}. Given number is palindrome")
else:
    print(f"{palindrome}. Given number isn't palindrome")

print("------------------------------------------------------------")

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for num in list1:
    if num % 2 != 0:
        list3.append(num)

for num in list2:
    if num % 2 == 0:
        list3.append(num)

print(f"result list: {list3}")

print("--------------------------------------------------------------")

number = int(input("write a number: "))

while number > 0:
    # get the last digit
    reminder = number % 10
    # remove the last digit and repeat loop
    number = number // 10
    print(reminder, end=" ")

print("----------------------------------------------------------------")

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

print("------------------------------------------------------")

for r in range(1, 11):
    for c in range(1,11 ):
        print(r * c, end=" ")
    print(" ")

print("--------------------------------------------------------")

for r in range(5, 0, -1):
    for c in range(1, r + 1):
        print("*", end=" ")
    print(" ")

print("----------------------------------------------------------")

base = int(input("write the base: "))
exp = int(input("write the power: "))

def exponent(base, exp):
    print(f"Base= {base}")
    print(f"Exponent= {exp}")

    base_1 = base
    for i in range(exp - 1):
        base = base * base_1
    print(f'{base_1} to the power of {exp}: {base}')

exponent(base,exp)