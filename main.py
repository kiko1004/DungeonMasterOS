from game_engine import *
import os

def initialize():
    print('Starting ...')
    if not os.path.exists('adventures'):
        print('Adventures folder does not exist, creating ...')
        os.makedirs('adventures')
    if input('Would you like to enter your character from DnDBeyond? y/n') == 'y':
        while True:
            try:
                char_number = input('Please enter character number: ')
                character = Character(char_number)
                print(f'You are {character.age} age {character.race} named {character.name}')
                return character
                break
            except:
                print('Please enter a valid character number!')
    else:
        print('You have chosen to skip this step. Continuing ...')
    return None

def choose_adventure():
    while True:
        choice = input('Would you like to load an adventure or create a new one? \n Enter "n" for new one of "l" for load:')
        if choice.lower() == 'n':
            adventure_name = input('Please enter adventure name: ')
            return adventure_name
        elif choice.lower() == 'l':
            onlyfiles = [f for f in os.listdir('adventures') if os.path.isfile(os.path.join('adventures', f))]


def main():
    character = initialize()




