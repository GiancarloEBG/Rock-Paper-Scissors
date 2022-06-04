import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors", "spock", "lizard"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Spock/Lizard or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Choose an option properly.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print("Computer picked: ", computer_pick + ".")

    if (user_input == "rock" and computer_pick == "scissors") or (user_input == "scissors" and computer_pick == "paper") or (user_input == "paper" and computer_pick == "rock"):
        print("You won!")
        user_wins += 1

    elif( user_input == "rock" and computer_pick == "paper") or (user_input == "scissors" and computer_pick == "rock") or (user_input == "paper" and computer_pick == "scissors"):
        print("You lost!")
        computer_wins += 1

    elif (user_input == "rock" and computer_pick == "lizard") or (user_input == "scissors" and computer_pick == "lizard") or (user_input == "paper" and computer_pick == "spock"):
        print("You won!")
        user_wins += 1

    elif (user_input == "lizard" and computer_pick == "rock") or (user_input == "lizard" and computer_pick == "scissors") or (user_input == "spock" and computer_pick == "paper"):
        print("You lost!")
        computer_wins += 1

    elif (user_input == "spock" and computer_pick == "rock") or (user_input == "spock" and computer_pick == "scissors") or (user_input == "lizard" and computer_pick == "spock") or (user_input == "lizard" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    
    elif (user_input == "rock" and computer_pick == "spock") or (user_input == "scissors" and computer_pick == "spock") or (user_input == "spock" and computer_pick == "lizard") or (user_input == "paper" and computer_pick == "lizard"):
        print("You lost!")
        computer_wins += 1

    else:
        print("DRAW")

print("You won ", user_wins, " times")
print("The computer won ", computer_wins, " times")
