import random

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# What you should consider in the game interactions
# Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# In your GitHub Codespaces, use the provided specifications to create prompts that can be utilized by GitHub Copilot to assist you in developing the minigame. Remember, GitHub Copilot uses comments to understand context and provide accurate suggestions during development.

# Check your work
# Run the minigame on the console with the python app.py command.
# At the prompt, type one of the game options: rock, paper, or scissors.
# The minigame should inform the player whether the player won, lost, or tied with the opponent.
# Choose to continue playing.
# At the prompt, type screen.
# The minigame should inform the player if the option entered by the player is invalid.
# Repeat steps 2 and 4 to play a few rounds and choose not to continue playing.
# Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.
# Congratulations on completing this challenge exercise! You've created a Python console minigame using GitHub Copilot.

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win"
    else:
        return "You lose"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        else:
            print("Invalid choice. Please try again.")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win":
            user_score += 1
        elif result == "You lose":
            computer_score += 1

        print(f"\nYour score: {user_score}")
        print(f"Computer score: {computer_score}")

        if not play_again():
            break

    print("\nGame over!")
    print(f"Your final score: {user_score}")
    print(f"Computer final score: {computer_score}")

play_game()