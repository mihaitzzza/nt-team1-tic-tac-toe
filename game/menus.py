from .modes import play, logger
from .player import display_winner


def main_menu():
    """
    Displays main menu options
    """           
    selection = ''                           
    while selection != '2':     
        print('\nMain Menu')
        print('----------')
        print('1. Play')  # play submenu function created below
        print('2. Exit')  # add more print lines for other submenus
        
        selection = input('>: ')
        if selection == '1':  # add an if check for the new menu added
            print('Selected Play')
            play_menu()  # call menu or feature function


def play_menu():
    """
    Displays play menu options
    """
    selection = '' 
    while selection != '3':
        print('\nPlay')
        print('----------')
        print('1. Vs Player')
        print('2. Vs Computer')
        print('3. Return to Main Menu')
        
        selection = input('>: ')
        if selection == '1':
            game_winner = play()
            display_winner(game_winner, logger)  

        elif selection == '2':
            select_difficulty_menu()


def select_difficulty_menu():
    """
    Displays CPU difficulties to choose from
    """
    selection = ''
    while selection != '4':
        print('\nChoose difficulty')
        print('----------')
        print('1. Easy')
        print('2. Medium')
        print('3. Hard')
        print('4. Go back')

        selection = input('>: ')
        if selection == '1':
            game_winner = play(cpu='easy')
            display_winner(game_winner, logger)
            break
        elif selection == '2':
            game_winner = play(cpu='medium')
            display_winner(game_winner, logger)
            break
        elif selection == '3':
            game_winner = play(cpu='hard')
            display_winner(game_winner, logger)
            break