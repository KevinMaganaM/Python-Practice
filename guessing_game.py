import random

secret_number = random.randint(1,10)
guess_count = 0
guess_limit = 3

print('Guess the secret number')
while guess_count < guess_limit:
    guess = int(input('Guess:'))
    guess_count += 1
    if guess == secret_number:
        print("That's right, you won!")
        break
else:
    print('Sorry, you failed!')
    print(f"The secret number is {secret_number}")