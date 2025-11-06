# 🎃 The Haunted Trick or Treat Night
# 👩‍💻 Created by Vicky for Programmiz October Challenge: "Trick, Treat & Code"
# 🕯️ A spooky, mysterious text adventure with random twists...

import time
import random

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
    slow_print("💀 Welcome to the Haunted Trick or Treat Night... Enter if you dare! 💀", 0.08)

def start_game():
    score = 0
    print_ascii_art()
    slow_print("🌫️ You step into the foggy streets of Ravenshade...")
    name = input("What is your name, wanderer? > ").strip().capitalize()
    slow_print(f"👁️ The spirits whisper... '{name}... you shouldn’t have come here...'")

    riddles = [
        ("I have keys but no locks, space but no rooms. You can enter but can't go outside. What am I?", "keyboard"),
        ("I can fly without wings. I cry without eyes. What am I?", "cloud"),
        ("I’m found in darkness but make no sound. What am I?", "shadow"),
        ("The more you take, the more you leave behind. What am I?", "footsteps"),
        ("What has a face and hands but no arms or legs?", "clock"),
        ("I can run but never walk, have a bed but never sleep. What am I?", "river"),
        ("What gets sharper the more you use it?", "your brain"),
        ("I am not alive but I grow. I don’t have lungs but I need air. What am I?", "fire"),
        ("I have a neck but no head. What am I?", "bottle"),
        ("What can’t talk but replies when spoken to?", "echo")
    ]

    while True:
        choice = input("\nDo you choose Trick or Treat? > ").lower()

        if choice == "trick":
            riddle, answer = random.choice(riddles)
            slow_print("🕯️ You chose Trick... The shadows close in...")
            time.sleep(1)
            user_answer = input(f"\n🧩 Riddle: {riddle}\n> ").lower()

            if answer in user_answer:
                slow_print("✨ Correct! The spirits whisper in approval... (+10 points)")
                score += 10
            else:
                slow_print("💀 WRONG! The spirits SCREAM your name in anger! (-5 points)")
                slow_print("⚠️ A cold wind chills your soul... You feel your life slipping away...")
                score -= 5

        elif choice == "treat":
            slow_print(f"🍬 You knock on a rotting door... creaaak... It opens slowly...")
            time.sleep(1)
            candy = input("🧙‍♀️ A witch offers you a glowing candy. Do you take it? (yes/no) > ").lower()

            if candy == "yes":
                outcome = random.choice(["sweet", "sour", "poisoned", "enchanted", "hand", "scream", "shadow"])
                if outcome == "sweet":
                    slow_print("😋 You eat it — it tastes sweet! The night feels calm... (+5 points)")
                    score += 5
                elif outcome == "enchanted":
                    slow_print("🌟 The candy glows! You hear whispers of ancient magic... (+10 points)")
                    score += 10
                elif outcome == "sour":
                    slow_print("😖 Eww... sour candy! Your face twists in disgust... (0 points)")
                elif outcome == "poisoned":
                    slow_print("☠️ The candy burns your tongue! It was poisoned! (-5 points)")
                    slow_print("⚠️ The witch cackles as your vision fades into black...")
                    score -= 5
                elif outcome == "hand":
                    slow_print("🫱 You drop the candy... it morphs into a *human hand*! (-10 points)")
                    slow_print("💀 It crawls away, whispering your name...")
                    score -= 10
                elif outcome == "scream":
                    slow_print("🩸 The candy SCREAMS as you bite it! The walls echo your name... (-7 points)")
                    score -= 7
                else:
                    slow_print("🌑 Your shadow detaches... It walks away laughing... (-5 points)")
                    score -= 5
            else:
                slow_print("😶 You refuse politely. The witch frowns and disappears in black smoke...")

        else:
            slow_print("👻 The spirits don’t understand your choice... Speak wisely next time!")
            continue

        slow_print(f"\n💀 Your current score: {score}")

        again = input("\nDo you dare to visit another house? (yes/no) > ").lower()
        if again != "yes":
            break

    end_banner = (
        "\n  ***************************************\n"
        + "  *           👻  GAME OVER  👻            *\n"
        + "  ***************************************\n"
    )
    print(end_banner)
    slow_print(f"🩸 Farewell, {name}... Final Score: {score}")
    if score < 0:
        slow_print("⚰️ The spirits have claimed your soul... Better luck in the afterlife.")
    else:
        slow_print("🌕 You survived the night... but Ravenshade remembers you...")

if __name__ == "__main__":
    start_game()
