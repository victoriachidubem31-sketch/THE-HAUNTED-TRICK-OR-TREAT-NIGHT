# 🎃 The Haunted Trick or Treat Night
# 👩‍💻 Created by Vicky for Programmiz October Challenge: "Trick, Treat & Code"
# Beginner-friendly text adventure game (no colors).

import time
import random

# Function to print text slowly for spooky effect
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to next line

# Function to print spooky ASCII title
def print_ascii_art():
    title = """
  ██████╗ ██╗  ██╗ █████╗ ██╗   ██╗███╗   ██╗██████╗ ███████╗
  ██╔══██╗██║  ██║██╔══██╗██║   ██║████╗  ██║██╔══██╗██╔════╝
  ██║  ██║███████║███████║██║   ██║██╔██╗ ██║██║  ██║█████╗  
  ██║  ██║██╔══██║██╔══██║██║   ██║██║╚██╗██║██║  ██║██╔══╝  
  ██████╔╝██║  ██║██║  ██║╚██████╔╝██║ ╚████║██████╔╝███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
"""
    print(title)
    slow_print("Welcome to the Haunted Trick or Treat Night...", 0.08)

# Start of the game
def start_game():
    score = 0
    print_ascii_art()
    slow_print("👻 Welcome, brave soul... to the haunted neighborhood of Ravenshade...")
    name = input("What is your name, wanderer? > ").strip().capitalize()
    slow_print(f"Ah, {name}... The spirits whisper your name already.")

    while True:
        choice = input("Do you choose Trick or Treat? > ").lower()

        if choice == "trick":
            slow_print("You chose Trick... How daring!")
            time.sleep(1)
            riddle_answer = input(
                "\nRiddle: I have keys but no locks. I have space but no rooms. You can enter but can't go outside. What am I? > "
            ).lower()

            if "keyboard" in riddle_answer:
                slow_print("Correct! The spirits smile upon you. (+10 points)")
                score += 10
            else:
                slow_print("Wrong! The spirits are displeased... (-5 points)")
                score -= 5

        elif choice == "treat":
            slow_print(f"You chose to go for Treat... How brave, {name}!")
            time.sleep(1)
            slow_print("You knock on a door... creaaak... It opens slowly...")
            candy = input("An old witch hands you a bowl of candies. Do you take one? (yes/no) > ").lower()

            if candy == "yes":
                outcome = random.choice(["sweet", "sour", "poisoned", "enchanted"])
                if outcome == "sweet":
                    slow_print("Yum! It was sweet candy! (+5 points)")
                    score += 5
                elif outcome == "enchanted":
                    slow_print("Whoa... the candy glows! It's enchanted! (+10 points)")
                    score += 10
                elif outcome == "sour":
                    slow_print("Eww... sour candy! (0 points)")
                else:
                    slow_print("Oh no! It's poisoned candy! (-5 points)")
                    score -= 5
            else:
                slow_print("You politely decline. The witch nods and vanishes in smoke...")

        else:
            slow_print("The spirits do not understand your choice... Try again.")
            continue

        # Show score after each round
        slow_print(f"Your score is now: {score}")

        # Ask to continue or end
        again = input("Do you dare to visit another house? (yes/no) > ").lower()
        if again != "yes":
            break

    # Ending banner
    end_banner = (
        "\n  ***************************************\n"
        + "  *             👻  THE END  👻            *\n"
        + "  ***************************************\n"
    )
    print(end_banner)
    slow_print(f"Game Over, {name}! Final Score: {score}")

# Run the game
if __name__ == "__main__":
    start_game()
