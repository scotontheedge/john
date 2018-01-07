"""
    User navigation for playing the quiz. Also the main file user uses to load the quiz menu.
"""
import os
from login import login, load_highscores
from register import register
from quiz import create_quiz


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """
    Description: Display the navigation menu
    """

    print('''
        a) Login and Play
        b) Register and Play
        c) View My High Scores
        d) View All High Scores
        e) Quit
    ''')

    choice = input("Please enter your choice: ")
    choice = choice.lower()
    if choice == 'a':
        cls()
        # Login user
        user = login()
        if user:
            # Create and play the quiz
            create_quiz(user)
            display_menu()
        else:
            print("User not yet registered.")
            display_menu()
    elif choice == 'b':
        cls()
        # Register user
        user = register()
        if user:
            # Create and play the quiz
            create_quiz(user)
            display_menu()
    elif choice == 'c':
        cls()
        user = login()
        if user:
            user.show_high_scores()
        display_menu()
    elif choice == 'd':
        cls()
        scores = load_highscores()
        if scores:
            scores.show_high_scores()
        else:
            print('\nNo high scores currently recorded.')
        display_menu()
    elif choice == 'e':
        print('Quit')
    else:
        display_menu()


# Clear the screen
cls()
# Call the display menu 
display_menu()
