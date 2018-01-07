"""
Description: Methods for logging in and loading high score tables
"""
# Include required python libraries 
import os
import pickle

# Global definitions
FILENAME = "storage/user.txt"
HIGHSCORES = "storage/highscores.txt"


def save_list(users):
    """
    Description:
        Save all user information to a user file

    Parameters:
        users: list of user object to save to file
    """

    # Open the file in overwrite(w+) and binary mode(b)
    with open(FILENAME, 'w+b') as f:
        # Use pickle to save the list of user objects to the file
        pickle.dump(users, f)


def check_list(users, user_name):
    """
    Description: Checks if the user name is in the users list

    Parameters:
        users: List of user objects
        user_name: Name of user to check for in the list

    Returns:
        The user if found or None if not found
    """
    for u in users:
        if u.user_name == user_name:
            return u

    return None


def get_list():
    """
    Description: Get list of user objects from file

    Returns:
        A list of user objects or an empty list if none found or file does not exist
    """
    # Check file exists
    if os.path.isfile(FILENAME):
        # Open file in read and binary mode
        with open(FILENAME, 'rb') as f:
            # Load list of user objects from file
            users = pickle.load(f)
            
            # Return list of user objects or an empty list if none
            return users if users else []

    # Return empty list if file does not exist
    return []


def load_user(user_name):
    """
    Description: Load a user

    Parameters:
        user_name: User to load

    Returns:
        The user object or None
    """
    users = get_list()

    return check_list(users, user_name)


def login():
    """
    Description: Login a user

    Return:
        The logged in user or None if not found
    """
    user_name = input("Enter user name: ")
    
    # Convert login name to lower case and attempt to load the user
    user = load_user(user_name.lower())

    return user


def save_highscores(scores):
    """
    Description: Save the all time highscores object to a file

    Parameters:
        scores: All time highscores
    """
    # Open file in overwrite(w+) and binary(b) mode
    with open(HIGHSCORES, 'w+b') as f:
        # Save the high scores to file
        pickle.dump(scores, f)


def load_highscores():
    """
    Description: Load the all time high scores object from file

    Return:
        The high scores object from file or None
    """
    if os.path.isfile(HIGHSCORES):
        # Open file
        with open(HIGHSCORES, 'rb') as f:
            # Load list of user objects from file
            scores = pickle.load(f)
            
            # Return high score object or None if not found
            return scores if scores else None

    # Return None if file does not exist
    return None
