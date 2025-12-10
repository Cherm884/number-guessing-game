import random
import time

def get_difficulty():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = int(input("Enter your choice: "))
        if choice in [1, 2, 3]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_chances(dificulty):
    if dificulty == 1:
        print("Great! You have selected the Easy difficulty level.")
        return 10
    elif dificulty == 2:
        print("Great! You have selected the Medium difficulty level.")
        return 5
    elif dificulty == 3:
        print("Great! You have selected the Hard difficulty level.")
        return 3
    
def get_hints(random_number,number):
    diff = abs(random_number - number)
    
    if diff <= 5:
        return "You're very close!"
    elif diff <= 10:
        return "You're close!"
    elif diff <= 20:
        return "You're far!"
    else:
        return "You're very far!"

def play_game(high_scores):
    difficulty = get_difficulty()
    chances =  get_chances(difficulty)
    
    print("Let's start the game!\n")
    
    random_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while chances > 0: 
        chances -= 1
        attempts += 1
        number = int(input("Enter your guess:"))
        

        if number > random_number:
            print(f"Incorrect! The number is less than {number}.")

        elif number < random_number:
            print(f"Incorrect! The number is greater than {number}.")
        else:
            time_taken = round(time.time() - start_time,2)
            print(f"Congratulations! You guessed the correct number in {attempts} attempts and {time_taken} seconds.")

            if difficulty not in high_scores or attempts < high_scores[difficulty]['attempts']:
                high_scores[difficulty] = {'attempts': attempts, 'time': time_taken}
                print("New high score! for this difficulty level.")
            return
        print("hint: ", get_hints(random_number,number))

        print(f"You have {chances} chances left.\n")

    print(f" Game Over! You ran out of chances.")
    print(f"The correct number was: {random_number}")


def main():
    high_scores = {}
    while True:
        play_game(high_scores)

        print("\nHigh Scores:")
        for diff, score in high_scores.items():
            level = {1: "Easy", 2: "Medium", 3: "Hard"}[diff]
            print(f"{level}: {score} attempts in {score['time']} seconds")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

main()