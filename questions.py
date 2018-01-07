"""
List of categories and difficulty levels and Dictionaries of questions and answers
"""

categories = ['Geography', 'History', 'Science', 'Sport', 'Music']
difficulty = ['Easy', 'Medium', 'Hard']

questions = {
    'Geography':
        {'Easy': {
            'questions': [
                "What is the capital of Finland?",
                "What is the capital of Scotland?",
                "What is the capital of France?",
            ],
            'answers': [
                {'choices': {'1': 'Helsinki', '2': 'Oslo', '3': 'Copenhagen', '4': 'Stockholm'}, 'answer': '1'},
                {'choices': {'1': 'Glasgow', '2': 'Edinburgh', '3': 'Aberdeen', '4': 'Dundee'}, 'answer': '2'},
                {'choices': {'1': 'Marseille', '2': 'Lyon', '3': 'Calais', '4': 'Paris'}, 'answer': '4'},
            ]
        },
            'Medium': {
                'questions': [
                    "What is the capital of Argentina?",
                    "What is the capital of Brasil?",
                    "What is the capital of Lithuania?",
                ],
                'answers': [
                    {'choices': {'1': 'Lima', '2': 'Montevideo', '3': 'Santiago', '4': 'Buenos Aires'}, 'answer': '4'},
                    {'choices': {'1': 'Rio De Jainero', '2': 'Brasilia', '3': 'Madrid', '4': 'Lima'}, 'answer': '2'},
                    {'choices': {'1': 'Helsinki', '2': 'Oslo', '3': 'Copenhagen', '4': 'Vilnius'}, 'answer': '4'},
                ]
            },
            'Hard': {
                'questions': [
                    "Which Scandinavian nation lies between Norway and Finland??",
                    "Magyars are the people of which country?",
                    "Within which country can two other independent countries be found??",
                ],
                'answers': [
                    {'choices': {'1': 'Sweden', '2': 'Latvia', '3': 'Denmark', '4': 'Estonia'}, 'answer': '1'},
                    {'choices': {'1': 'Hungary', '2': 'Slovakia', '3': 'Romania', '4': 'Croatia'}, 'answer': '1'},
                    {'choices': {'1': 'Russia', '2': 'South Africa', '3': 'Italy', '4': 'Canada'}, 'answer': '3'},
                ]
            },
        },
    'History':
        {'Easy': {
            'questions': [
                "Which famous military leader defeated Napoleon at the Battle of Waterloo?",
                "During which battle did Admiral Lord Nelson receive the bullet wound that would lead to his death?",
                "When did World War I begin?",
            ],
            'answers': [
                {'choices': {'1': 'Kitchener', '2': 'Gordon', '3': 'Wellington', '4': 'Washington'}, 'answer': '3'},
                {'choices': {'1': 'Nile', '2': 'Trafalgar', '3': 'Copenhagen', '4': 'Jutland'}, 'answer': '2'},
                {'choices': {'1': '1913', '2': '1945', '3': '1918', '4': '1914'}, 'answer': '4'},
            ]
        },
            'Medium': {
                'questions': [
                    "Which Admiral led the British Royal Navy during the Battle of the Nile in 1798?",
                    "What was Wolfgan Mozart's middle name?",
                    "In mythology, Romulus and Remus were brought up by which animal?",
                ],
                'answers': [
                    {'choices': {'1': 'Hawke', '2': 'Nelson', '3': 'Drake', '4': 'Smith'}, 'answer': '2'},
                    {'choices': {'1': 'George', '2': 'Johan', '3': 'Ludwig', '4': 'Amadeus'}, 'answer': '4'},
                    {'choices': {'1': 'Lion', '2': 'Dog', '3': 'Wolf', '4': 'Monkey'}, 'answer': '3'},
                ]
            },
            'Hard': {
                'questions': [
                    "Nostradamus was famous for making what??",
                    "Who established the Church of England?",
                    "Who was the first female to fly solo from Great Britain to Australia??",
                ],
                'answers': [
                    {'choices': {'1': 'Churches', '2': 'Predictions', '3': 'Maps', '4': 'Bridges'}, 'answer': '2'},
                    {'choices': {'1': 'Elizabeth I', '2': 'Henry VIII', '3': 'George III', '4': 'Mary I'},
                     'answer': '2'},
                    {'choices': {'1': 'Felicity Spearman', '2': 'Amelia Earhart', '3': 'Blanche Scott',
                                 '4': 'Amy Johnson'}, 'answer': '4'},
                ]
            },
        },
    'Science':
        {'Easy': {
            'questions': [
                "A leveret is the young of which animal?",
                "Which chemical element, number 11 in the Periodic table, has the symbol Na?",
                "Diamonds are a form of which chemical element?",
            ],
            'answers': [
                {'choices': {'1': 'Deer', '2': 'Rabbit', '3': 'Hare', '4': 'Fox'}, 'answer': '3'},
                {'choices': {'1': 'Sulphur', '2': 'Nitrogen', '3': 'Nickel', '4': 'Sodium'}, 'answer': '4'},
                {'choices': {'1': 'Silver', '2': 'Gold', '3': 'Carbon', '4': 'Mercury'}, 'answer': '3'},
            ]
        },
            'Medium': {
                'questions': [
                    "Dry ice is a frozen form of which gas?",
                    "Where are human triceps muscles to be found?",
                    "What is the brightest star in the night sky?",
                ],
                'answers': [
                    {'choices': {'1': 'Oxygen', '2': 'Hydrogen', '3': 'Sulphur Dioxide', '4': 'Carbon Dioxide'},
                     'answer': '4'},
                    {'choices': {'1': 'Arms', '2': 'Legs', '3': 'Back', '4': 'Neck'}, 'answer': '1'},
                    {'choices': {'1': 'Vega', '2': 'Castor', '3': 'Sirius', '4': 'Rigel'}, 'answer': '3'},
                ]
            },
            'Hard': {
                'questions': [
                    "If you wanted to separate the different hydrocarbons in crude oil what process would you use?",
                    "What is the fruit of the tropical plant Ananas comosus?",
                    "What is manufactured by the Haber process?",
                ],
                'answers': [
                    {'choices': {'1': 'Fractional Distillation', '2': 'Chromotography', '3': 'Lime Water Test',
                                 '4': 'Osmosis'}, 'answer': '1'},
                    {'choices': {'1': 'Pear', '2': 'Olive', '3': 'Banana', '4': 'Pineapple'}, 'answer': '4'},
                    {'choices': {'1': 'Iron', '2': 'Oil', '3': 'Ammonia', '4': 'Coal'}, 'answer': '3'},
                ]
            },
        },
    'Sport':
        {'Easy': {
            'questions': [
                "What team plays at Old Trafford?",
                "What is the nickname of West Ham Utd?",
                "How many players in a basketball match?",
            ],
            'answers': [
                {'choices': {'1': 'Manchester City', '2': 'Manchester United', '3': 'Liverpool', '4': 'Arsenal'},
                 'answer': '2'},
                {'choices': {'1': 'Hatters', '2': 'Gunners', '3': 'Red Devils', '4': 'Hammers'}, 'answer': '4'},
                {'choices': {'1': '5', '2': '11', '3': '10', '4': '8'}, 'answer': '3'},
            ]
        },
            'Medium': {
                'questions': [
                    "What horse won the Grand National 3 Times?",
                    "Who won the 1978 World Cup?",
                    "What is tennis player Andy Murray mother's name?",
                ],
                'answers': [
                    {'choices': {'1': 'Red Rum', '2': 'White Whisky', '3': 'Brown Brandy', '4': 'Gree Gin'},
                     'answer': '1'},
                    {'choices': {'1': 'Brazil', '2': 'Argentina', '3': 'Italy', '4': 'France'}, 'answer': '2'},
                    {'choices': {'1': 'Julia', '2': 'Judy', '3': 'Jessie', '4': 'Jane'}, 'answer': '2'},
                ]
            },
            'Hard': {
                'questions': [
                    "What snooker player has won the most title events?",
                    "What American football team play at Century Link Field?",
                    "What rugby team are known as the Springboks?",
                ],
                'answers': [
                    {'choices': {'1': 'Steve Davies', '2': "Ronnie O'Sullivan", '3': 'Stephen Hendry',
                                 '4': 'John Higgins'}, 'answer': '3'},
                    {'choices': {'1': 'Pittburg Steelers', '2': 'Seattle Seahawks', '3': 'New England Patriots',
                                 '4': 'Chicago Bears'}, 'answer': '2'},
                    {'choices': {'1': 'South Africa', '2': 'Australia', '3': 'Argentina', '4': 'Canada'},
                     'answer': '1'},
                ]
            },
        },
    'Music':
        {'Easy': {
            'questions': [
                "The musical Mamma Mia is based on the music of which band?",
                "Which band sang Livin' On A Prayer?",
                "Which group sung about a Yellow Submarine?",
            ],
            'answers': [
                {'choices': {'1': 'Spice Girls', '2': 'ABBA', '3': 'The Mamas And Papas', '4': 'The Jacksons'},
                 'answer': '2'},
                {'choices': {'1': "Guns'n'Roses", '2': 'AC/DC', '3': 'Bon Jovi', '4': 'Iron Maiden'}, 'answer': '3'},
                {'choices': {'1': 'Oasis', '2': 'The Beatles', '3': 'UB40', '4': 'The Who'}, 'answer': '2'},
            ]
        },
            'Medium': {
                'questions': [
                    "What nationality is singer Bryan Adams?",
                    "Which of these instruments is a percussion instrument?",
                    "What was the name of Michael Jackson's pet Chimpanzee?",
                ],
                'answers': [
                    {'choices': {'1': 'English', '2': 'American', '3': 'Australian', '4': 'Canadian'}, 'answer': '4'},
                    {'choices': {'1': 'Trumpet', '2': 'Euphonium', '3': 'Viola', '4': 'Glockenspiel'}, 'answer': '4'},
                    {'choices': {'1': 'Champagne', '2': 'Fizz', '3': 'Shampoo', '4': 'Bubbles'}, 'answer': '4'},
                ]
            },
            'Hard': {
                'questions': [
                    "What Sonny and Cher song was a hit in the 1980s for UB40 and Chrissie Hynde?",
                    "Which female pop star hit the headlines in 2007 when she shaved her head?",
                    "Who was The Beatles' manager?",
                ],
                'answers': [
                    {'choices': {'1': "I Can't Help Falling In Love With You", '2': 'I Got You Babe',
                                 '3': 'Red Red Wine', '4': "Don't Get Me Wrong"}, 'answer': '2'},
                    {'choices': {'1': 'Madonna', '2': 'Kylie Minogue', '3': 'Britney Spears', '4': 'Lady Gaga'},
                     'answer': '3'},
                    {'choices': {'1': 'Brian Epstein', '2': 'Paul McCartney', '3': 'Pete Best', '4': 'Cilla Black'},
                     'answer': '1'},
                ]
            },
        },
}
