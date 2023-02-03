from question import Question
import json
import random
class QuestionLibrary:
    def __init__(self, filename='trivia.json'):
        """Reads the file and assigns the questions into an instance variable"""
        with open(filename, 'r') as f: # Open file as read
            questions_data = json.load(f) # Load data into variable called questions_data
        self.questions = [Question(**q) for q in questions_data] # Creates a list of Question objects by passing the data into the Question class
    
    def __len__(self):
        """Allows to search for length"""
        return len(self.questions)
    
    def get_categories(self):
        """Returns a list of categories"""
        list = [] # Define empty list
        for question in self.questions: # For each object in self.questions, if the category is not already added, add it
            if question.category not in list:
                list.append(question.category)
        return list
    
    def get_questions(self, category=None, difficulty=None, number=250):
        """Return radomized questions based on input"""
        shuffled_questions = self.questions # Shuffles the questions
        random.shuffle(shuffled_questions)
        filtered_questions = [] # Defines an empty list to store the questions
        if category and category not in self.get_categories(): # If category is not in the list of categories, raise value error
            raise ValueError("Invalid category")
        if difficulty and difficulty not in ["easy", "medium", "hard"]: # If difficulty isn't listed, ignore it
            difficulty = None
        for question in shuffled_questions: # For loop for each question, add the question to the list until it reaches the number given in the parameter
            if not category or question.category == category:
                if not difficulty or question.difficulty == difficulty:
                    filtered_questions.append(question)
                    if len(filtered_questions) == number:
                        break
        return filtered_questions