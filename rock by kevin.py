# Made by Kevin Perez
import time
import random

print('Welcome to the game of Rock, Paper, Scissors. You must win 3 times without any losses.')

def choices():
    x = 0
    while x < 3:
        pl_choice = input('Choose r for Rock, p for Paper, or s for Scissors: ')
        option = ['r','p','s']
        com_choice = random.choice(option)
        
        if pl_choice == 'r' or pl_choice == 'p' or pl_choice == 's':

            if pl_choice == com_choice:
                time.sleep(0.8)
                print(f'It\'s a tie!!!! You both chose {answer(pl_choice)} ')
                continue
            
            elif win(pl_choice,com_choice):
                time.sleep(0.8)
                print(f'{answer(pl_choice).capitalize()} beats {answer(com_choice)}, you WIN!!!')
                x = x + 1
                if x == 3:
                    time.sleep(0.8)
                    return 'WOW you WIN, You\'re really lucky!!!!'
                continue
            
            elif pl_choice != win(pl_choice, com_choice):
                time.sleep(0.5)
                print(f'You chose {answer(pl_choice)} but the computer chose {answer(com_choice)}. You lose, better luck next time ')
                time.sleep(1)
                return 'Bye.'
        
        else:
            print('Enter a proper choice')
            continue


def win(pl_choice, com_choice):
    if (pl_choice == 'r' and com_choice == 's') or (pl_choice == 'p' and com_choice == 'r') or (pl_choice == 's' and com_choice == 'p'):
        return True

def answer(pl_choice):
    if pl_choice == 'r':
        return 'rock'
    elif pl_choice == 'p':
        return 'paper'
    return 'scissors'

def answer(com_choice):
    if com_choice == 'r':
        return 'rock'
    elif com_choice == 'p':
        return 'paper'
    return 'scissors'

print(choices())