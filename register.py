"""
    methods to register a user
"""

from classes import User
from login import get_list, check_list, save_list


def new_user(user):
    """
    Description: Create a new user if it doesn't already exist

    Parameters:
        user: User object to be creates
    """
    # Check if user exists
    users = get_list()
    user_exist = check_list(users, user.user_name)
    if not user_exist:
        # User doesn't exist in the list, so create and save
        users.append(user)
        save_list(users)
    else:
        # User already exists
        print("User {} already exists.".format(user.user_name))


def register():
    """
    Description: Capture user details and try to create a user

    Returns:
        Returns a new user
    """
    # Enter User Details
    name = input("Please enter your name: ")

    # Loop rounf until user inputs valid registration data
    while True:
        age = input("Please enter you age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Age must be a number. Try again.")
    while True:
        year_group = input("Please enter your year group: ")
        if year_group.isdigit():
            year_group = int(year_group)
            break
        else:
            print("Year group must be a number. Try again.")

    # Create User object
    user = User(name, age, year_group)
    print("Your user name is {} \n".format(user))

    # Attempt to create and save the user
    new_user(user)

    return user

