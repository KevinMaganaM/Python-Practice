secret_number = 8
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