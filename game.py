from question_library import QuestionLibrary
class Game:
    def __init__(self, filename="trivia.json", category=None, difficulty=None, number=250):
        self.library = QuestionLibrary(filename) # Creates instance of QuestionLibrary class
        self.questions = self.library.get_questions(category, difficulty, number) # Creates instance of object of questions
        self.score = 0 # Sets a default score

    def play(self):
        """Uses for loop to loop through each iteration of game"""
        for question in self.questions:
            print(question.question) # Print question
            print(question.answers)# Print answer
            print(f'Difficulty: {question.difficulty}') # Print difficulty
            while True: # While loop to confirm user input is either 1, 2, 3, or 4
                player_input = input("Enter the correct answer: ")
                if player_input in ["1", "2", "3", "4"]:
                    player_input = int(player_input)
                    break
                print("Invalid input. Please enter a number between 1 and 4.")
            score_increment = 1 if question.difficulty == 'easy' else 2 if question.difficulty == 'medium' else 3 # score increment decided based on difficulty. Will be added to score later
            if player_input == question.answer_id: # If player input is correct, add score by score increment
                self.score += score_increment
                print("That is correct!")
                print(f'You\'re score is {self.score}') # Display score
            else: # If player input is incorrect, display the correct answer
                print("That is incorrect")
                print(f'The correct answer was {question.answers[question.answer_index]}')
                print(f'You\'re score is {self.score}') # Display score

            print()
            print('-----------------------------------------')
            print()