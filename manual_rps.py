from ast import While
import random

class RPS:

    def __init__(self, list_choices):
        self.list_choices = list_choices
    pass


    def get_computer_choice(self, list_choices):
        return random.choice(list_choices)

    pass



    def get_user_choice(self,list_choices):
        while True:
            user_input = input('Rock, Paper, Scissors!\nWhat do you choose?:\n').capitalize()
            if user_input not in list_choices:
                print('\nPlease enter either Rock, Paper or Scissors.')
            else:
                return user_input
    
    pass


    def get_winner(self, user_choice, computer_choice):
        if user_choice == 'Rock' and computer_choice == 'Scissors':
            return 'You win!'
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            return 'You win!'
        elif user_choice == 'Scissors' and computer_choice == 'Rock':
            return 'You lose.'
        elif user_choice == 'Paper' and computer_choice == 'Scissors':
            return 'You lose.'
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            return 'You win!'
        elif user_choice == 'Rock' and computer_choice == 'Paper':
            return 'You lose.'
        else:
            return 'It\'s a draw!'

    pass


    def play(self):
        computer_choice = self.get_computer_choice(list_choices)
        #print(computer_choice)
        user_choice = self.get_user_choice(list_choices)
        get_winner = self.get_winner(user_choice, computer_choice)
        print(f'\nComputer chose {computer_choice}.')
        print(f'\n{get_winner}')
    pass

list_choices=['Rock', 'Paper', 'Scissors']
p = RPS(list_choices)
p.play()