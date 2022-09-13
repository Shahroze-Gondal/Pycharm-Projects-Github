# Rock Paper Scissors Game
import random
def get_choices():
    player_choice = input('Enter a choice: (rock, paper, scissors):')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices
def check_win(player, computer):
    print(f"You chose: {player} Computer Chose: {computer}")
    if player == computer:
        return "It's a tie"
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes Scissors! You Win'
        else:
            return 'Paper covers rock! you lost'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! You win'
        else:
            return 'Scissors Cut paper! You lost'
    elif player == 'scissors':
        if computer == 'rock':
            return 'Rock smashes scissors! You lost'
        else:
            return 'Scissors Cut paper! You win'
choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)