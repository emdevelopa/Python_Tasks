import random

#Function for Computer Mode
def computer_mode():
    choices = ["rock", "paper", "scissors"]

    while True:
        players_choice = input("Enter a choice: ").lower()


        # Check Players Choice If Valid
        if players_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # get random choice for computer
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if players_choice == computer_choice:
            print("It's a tie!\n")
        elif ((players_choice == "rock" and computer_choice == "scissors") or
              (players_choice == "scissors" and computer_choice == "paper") or
                (players_choice == "paper" and computer_choice == "rock")):
            print("You win!")

        else:
            print("you lose!")
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


# Function for  Two Players Mode
def Two_Players():
    choices = ["rock", "paper", "scissors"]

    while True:
        player_one = input(
            "Player 1, enter your choice (rock, paper, scissors): ")

        if player_one not in choices:
            print("Invalid Choice by Player One. Try again")
            continue

        # Clear Sreen For Privacy
        # print("\n" * 50)

        player_two = input(
            "Player 2, enter your choice (rock, paper, scissors): ")

        if player_two not in choices:
            print("Invalid Choice by Player Two. Try again.")
            continue

            print(f"Player One Chose: {player_one}")
            print(f"Player Two Chose: {player_two}")

        if player_one == player_two:
            print("It's ties!\n")

        # Check For Player One wins
        elif ((player_one == "rock" and player_two == "scissors") or (player_one == "paper" and player_two == "rock") or (player_one == "scissors" and player_two == "paper")):
            print("Player One win!")
        else:
            print("Player Two wins")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks For Playing...")
            break


while True:
    print("WELCOME TO ROCK PAPER SCISSORS")
    print("1. Play with computer.")
    print("2. Two Players")
    print("3. Exit Game")

    select_menu = int(input("select an option from menu above: "))
    
    if select_menu == 1:
        computer_mode()
    
    if select_menu == 2:
        Two_Players()

    if select_menu == 3:
        print("Exiting game now....")
        break





 