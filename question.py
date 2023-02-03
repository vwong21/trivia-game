import random
class Question:
    """Assigns the question, answers, category and difficulty as an instance in the Question class"""
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        if type(question)!= str or type(correct_answer) != str or type(category) != str: # If question, correct_answer, or category is not a string, raise a type error
            raise TypeError("Must be string")
        if difficulty not in ["easy", "medium", "hard"]: # If difficulty is not easy, meduim or hard, raise an attribute error
            raise AttributeError("Enter either easy, medium or hard")
        if type(incorrect_answers) != list: # If incorrect_answers is not a list, raise a type error
            raise TypeError("Must be a list")
        self.question = question # Assigns intances of itself
        self.category = category
        self.difficulty = difficulty
        self.answers = incorrect_answers # Creates instance of answers and assigns the list of incorrect answers to it
        self.answers.insert(0, correct_answer) # Inserts the correct answer into the answer list
        random.shuffle(self.answers) # Shuffles the list
        self.answer_index = self.answers.index(correct_answer) # Creates an instance of the index of the correct answer
        self.answer_id = int(self.answer_index + 1) # Creates another instance of the index plus one
    
    def __str__(self):
        """Returns question, answer and indices"""
        answers_str = '\n'.join(f'{i + 1} {answer}' for i, answer in enumerate(self.answers)) # Creates an answer string using the answer and index + 1.
        return f'{self.question}\n{answers_str}'
