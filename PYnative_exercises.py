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