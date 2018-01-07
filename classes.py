"""
Description: Classes used in the quiz app.

Classes:
    User: User details and individual high_scores
    Quiz: Sets up and manages the quiz itself
    HighScores: The all time high score tables
"""


class User():
    """
    Class to manage user information, high scores and number of plays.
    """

    def __init__(self, n, a=15, yg=11):
        """Initialise internal variables using name, age and year group info"""
        self.name = n
        self.age = a
        self.year_group = yg
        self.user_name = "{0}{1}".format(n[:3].lower(), a)
        # Create empty play and high_score dictionaries
        self.plays = {}
        self.high_scores = {}

    def __str__(self):
        """
        Description: String method to return user name

        Returns:
            Returns the user_name
        """
        return self.user_name

    def add_high_score(self, category, difficulty, score):
        """
        Description: Check and add a new highscore for the user

        Parameters:
            category: The questions category
            difficulty: The questions difficulty
            score: The quiz score
        """
        # Check if a high score has been created for the category/difficulty
        high_score = self.high_scores.get(category + ' - ' + difficulty, 0)

        # If a high score has not been create or the new score is better then set a new high score
        if high_score < score:
            print("\nCongratulations. A new high score for {}-{}!!!\n".format(category, difficulty))
            self.high_scores[category + ' - ' + difficulty] = score

    def get_high_score(self, category, difficulty):
        """
        Description: Retrieves the users highscore for the category and difficulty

        Parameters:
            category: The questions category
            difficulty: The questions difficulty

        Returns:
            The high score or 0 if none set

        """
        return self.high_scores.get(category + difficulty, 0)

    def add_play(self, category, difficulty):
        """
        Description: Increments the number of user plays for the category/difficulty

        Parameters:
            category: The questions category
            difficulty: The questions difficulty
        """
        plays = self.plays.get(category + ' - ' + difficulty, 0)
        self.plays[category + ' - ' + difficulty] = plays + 1

    def get_plays(self, category, difficulty):
        """
        Description: Retrieves the number of user plays for the category and difficulty

        Parameters:
            category: The questions category
            difficulty: The questions difficulty

        Returns:
            The number of user plays for the category/difficulty or 0 if none set
        """

        return self.plays.get(category + ' - ' + difficulty, 0)

    def show_high_scores(self):
        """
        Description:
            Displays the users high scores for each category/difficulty
        """
        print("\n{} High Score Table\n".format(self.name.title()))

        # Iterate the high_scores dictionary and print the set high scores and the number of plays
        for key, value in self.high_scores.items():
            print("{}: {} is your high score from {} attempt(s).".format(key, value, self.plays.get(key, 0)))


class Quiz():
    """
    Class used to run the quiz. It asks the questions, provides choices, answers and scores.
    """

    def __init__(self, questions, answers):
        """
        Description: Initialise the Quiz object with passed in and default values

        Parameters:
            questions: The list of questions to be asked.
            answers: The list of answers to the questions.
        """
        self.questions = questions
        self.answers = answers
        self.score = 0
        self.asked = 0

    def play(self):
        """
        Description: Method to be called to play the quiz
        """
        # Zip allows us to iterate over two lists and assign the question and answer to variables
        for q, a in zip(self.questions, self.answers):
            self.ask_question(q, a)
            self.select_answer(a)

        print ("You scored {0}/{1}".format(self.score, self.asked))

    def ask_question(self, question, answers):
        """
        Description: Asks a quiz question

        Parameters:
            question: The question to be asked
            answers: Dictionary of answer options and the correct answer
        """
        # Ask the question
        print(question)
        # Increment the questions asked counter
        self.asked += 1
        # Display the multiple choice options from the answers dictionary
        for key, option in answers['choices'].items():
            print("{}. {}".format(key, option))

    def select_answer(self, answer):
        """
        Description: Ask the user to select an answer.

        Parameters:
            answer: The correct answer
        """
        choice = input("Please enter your answer: ")

        # Check to see if the user has the answer correct
        key = answer['answer']
        if choice == key:
            # The answer is correct so increment the score
            self.score += 1
            print("Correct! The answer is {}. {}\n".format(key, answer['choices'][key]))
        else:
            # print("Wrong! The answer is {}. {}\n".format(key, answer['choices'][key]))
            print("Sorry Wrong Answer!\n")


class HighScores():
    """
    Class used to manage quiz high score tables.
    """

    def __init__(self):
        """
        Description: Initialise the HighScores object

        """
        self.high_scores = {}

    def add_high_score(self, category, difficulty, score, user):
        """
        Description: Check and add a score to the all time highscore table

        Parameters:
            category: The questions category
            difficulty: The questions difficulty
            score: The score
            user: User object submitting the score
        """
        # Check if high score for the category/difficulty exists otherwise set to None
        high = self.high_scores.get(category + ' - ' + difficulty, None)

        # If there is not a high score or the new score beats the old one then create a new high score entry
        if not high or high[1] < score:
            print(
                "\nCongratulations. Your high score for {}-{} has been added to the All Time Leader Board!!!\n".format(
                    category, difficulty))
            self.high_scores[category + ' - ' + difficulty] = [user, score]

    def show_high_scores(self):
        """
        Description: Display all the all time leader board scores
        """
        print("\nAll Time High Score Table\n")
        # Iterate the high score dictionary and show the best scores for each category/difficulty
        for key, value in self.high_scores.items():
            # avg = round(value/plays,2) if value and plays else 0
            print("{}: {} scored {} from {} attempt(s).".format(key, value[0].name.title(), value[1],
                                                                value[0].plays.get(key, 0)))
