import random
import json

class Triviagame:
    def __init__(self, user):
        self.user = user
        self.score = 0

    def view_file(self):
        try:
            with open("trivals.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("This json file doesn't exit.")
            return []      

    def display_game(self):
        print('-'*35)
        print('WELCOME TO OUR TRIVIA GAME'.center(35))
        print("Let's see how smart you're!".center(37))
        print('-'*35)
        print(f"Welcome {self.user.title()} to our gaming session.\n")

        print("""Rules and Regulations:
    1. This exercise is a 20 software engineering questions.
    2. You're to pick one option by typing 1, 2, 3, or 4 per question or the option text in words.
    3. You'll have a maximum of 10mins to attempt all questions.
    4. You cannot skip a question to come back to it later.
    5. If you exit the game before its finishes, you'll be scored only for the questions attempted.
    6. To exit the game at any point, type 'exit'.
    7. Goodluck and see you at the top!""")

    def play_game(self):
        trival = self.view_file()

        if not trival:
            raise ValueError("NOGHEFE")
            # print('No questions available')
            # return
    
        random.shuffle(trival)

        for number, question in enumerate(trival, start=1):

            print("\n" + "-" * 50)
            print(f"Question {number}:")
            print(question["question"])
            print()

            # Randomize the options
            options = question["options"].copy()
            random.shuffle(options)

            # Display the options
            for option_number, option in enumerate(options, start=1):
                print(f"{option_number}. {option}")
            # try:
            while True:
                prompt = input("\nWhat's your answer? ").strip()
                if prompt.lower() == 'exit':
                    print("You exited the game.")
                    # return
                    print("\n" + "=" * 50)
                    print("QUIZ SCORE!")
                    print(f"Player: {self.user}")
                    print(f"Your score: {self.score}/{len(trival)}")
                    print("=" * 50)
                    exit(1)

                    # Check if the input is a number
                if prompt.isdigit():
                    option_number = int(prompt)

                    # Make sure the number is actually one of the options
                    if 1 <= option_number <= len(options):
                        selected_answer = options[option_number - 1]
                        break
                    else:
                        print(f"Invalid option. Please choose a number between 1 and {len(options)}.")

                # Otherwise, treat the input as answer text
                else:
                    # Check whether the typed text matches one of the options
                    matching_option = next(
                        (option for option in options if option.lower() == prompt.lower()),
                        None
                    )

                    if matching_option is not None:
                        selected_answer = matching_option
                        break

                    print("Invalid answer. Please enter an option number or the answer text.")

            # At this point, we have a valid option/answer
            if selected_answer.lower() == question["answer"].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect")
                print(f"The correct answer was: {question['answer']}")
        print("\n" + "=" * 50)
        print("QUIZ COMPLETE!")
        print(f"Player: {self.user}")
        print(f"Your score: {self.score}/{len(trival)}")
        print("=" * 50)
        exit(1)


name = input("What's your name? ").strip().capitalize()
user = Triviagame(name)
user.display_game()
ready = input("Are you ready to start your game? ")
while True:
    if ready.lower() == 'yes':
        user.play_game()
    elif ready.lower() == 'no':
        print("Goodbye dullard! Lol....")
        break
    else:
        print("Type 'yes' or 'no' to continue.")
        ready = input("Are you ready to start your game? ")

