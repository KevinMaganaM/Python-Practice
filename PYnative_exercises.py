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