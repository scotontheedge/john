"""
Main quiz management logic. Creates the classes and manages the flow through the application.
"""

# Import classes to be used
from classes import Quiz, HighScores

# Import methods to be used
from login import get_list, check_list, save_list, load_highscores, save_highscores

# Import list and dictionary data
from questions import questions, categories, difficulty


def update_user(user):
    """
    Description: Save the user object

    Parameters:
        user: The user object
    """

    # Get the list of users
    users = get_list()
    # Check if the user exists in the list of user objects
    user_exist = check_list(users, user.user_name)
    if user_exist:
        # If the user exists replace the old object in the list with the new one and save to file
        users.remove(user_exist)
        users.append(user)
        save_list(users)


def create_questions(category, difficulty):
    """
    Description: Retrieves the questions and answers for the chosen category/difficulty

    Parameters:
        category: The questions category
        difficulty: The questions difficulty

    Returns:
        A tuple containing the list of questions and the list of answers with dictionaries of choices and correct answers
    """
    return questions[category][difficulty]['questions'], questions[category][difficulty]['answers']


# noinspection PyShadowingNames
def create_quiz(user):
    """
    Description: Create, play the quiz and save user and high score info

    Parameters:
        user: The user playing the quiz

    """
    # Ask the user to choose a category
    cat = choose_category()
    # Ask the user to choose the question difficulty
    diff = choose_difficulty()
    # Create the questions and answers based on user requested category/difficulty 
    questions, answers = create_questions(cat, diff)

    # Tell the user their previous scores and number of attempts at this category/difficulty
    print("\nYou've had {} attempts at this category/difficulty and your current high score is {}\n" \
          .format(user.get_plays(cat, diff), user.get_high_score(cat, diff)))
    # Create a Quiz object by passing in the questions and answers to play
    quiz = Quiz(questions, answers)
    # Play the quiz
    quiz.play()
    # Increment the number of play counts for the user for the category/difficulty level
    user.add_play(cat, diff)
    # Check and add any user high score updates for the category/difficulty level
    user.add_high_score(cat, diff, quiz.score)

    # Load the all time high score table
    scores = load_highscores()

    if not scores:
        # No all time high scores yet created, so create one
        scores = HighScores()

    # Check and add the score if a new record
    scores.add_high_score(cat, diff, quiz.score, user)

    # Save the high score table
    save_highscores(scores)

    # Update user plays and high score info
    update_user(user)


def choose_category():
    """
    Description: Ask the user to choose a question category

    Returns:
        The category name from the categories list

    """
    # Set a 1-indexed counter
    c_count = 1
    # Display the categories using the counter and category name
    for c in categories:
        print("{}. {}".format(c_count, c))
        # Increment the counter
        c_count += 1

    # Ask the user to choose the category
    cat = int(input("Choose Category: "))
    # Ensure the choice is one of the category number
    # The range()/len() methods are used to check the number of values in the category
    if cat not in range(1, len(categories) + 1):
        # Force the user to choose again if an invalid category
        choose_category()

    print("\n")

    # Return the category and need to take 1 away from the user selection as 0-Based index
    return categories[cat - 1]


def choose_difficulty():
    """
    Description: Ask the user to choose a question difficulty

    Returns:
        The difficulty name from the difficulty list

    """
    # Set a 1-indexed counter
    d_count = 1
    # Display the difficulties using the counter and difficulty name
    for d in difficulty:
        print("{}. {}".format(d_count, d))
        # Increment the counter
        d_count += 1

    # Ask the user to choose the difficulty
    diff = int(input("Choose Difficulty: "))
    # Ensure the choice is one of the difficulty numbers
    # The range()/len() methods are used to check the number of values in the difficulties
    if diff not in range(1, len(difficulty) + 1):
        choose_difficulty()

    print("\n")
    # Return the difficulty and need to take 1 away from the user selection as 0-Based index
    return difficulty[diff - 1]
