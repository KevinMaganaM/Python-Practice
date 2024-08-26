import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    result = ''

    if win(user, computer) == "Draw":
        result = "Draw"
    elif win(user, computer):
        result = 'Youw won!'
    else:
        result = "You lost :("
    print(result)
    

def win(player, opponent):
    if player == 'r' and opponent == 'p' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p':
        return True
    elif player == opponent:
        return "Draw"
    else:
        return False

play()