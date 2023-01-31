import random

game_mode = input("\nChoose gamemode: [casual] or [competitive]: ")
generated_number = random.randint(1,100)

if game_mode == "casual":
    #rules
    print("\nRules of [casual] mode:\n✔ You have unlimited tries\n✔ You can use a hint")
    print()
    #player guess
    player_guess = input("\nGuess the number x(1-100) or receive a [hint]: ")
    #sc
    while player_guess!=generated_number:

        if player_guess == "hint":

            if generated_number % 2 == 0:
                print("Number x(1,100) is EVEN!\n")
            else:
                print("Number x(1,100) is ODD\n")

        elif generated_number>int(player_guess):
            print(f"Your guess is wrong. The number x is greater than {int(player_guess)}")

        elif generated_number<int(player_guess):
            print(f"Your guess is wrong. The number x is less than {int(player_guess)}")

        elif generated_number == int(player_guess):
            print(f"Congratulations! You guessed right! The number x is {generated_number}")
            break

        player_guess = input("Try again: ")

elif game_mode == "competitive":
    points = 650
    print("\nRules of [competitive] mode:\n✔ You have 650 starting points and lose 50 for every wrong answer\n✔ You do not have any additional hints.")
    player_guess = int(input("\nGuess the number x(1-100): "))

    while player_guess != generated_number:

        if generated_number>int(player_guess):
            print(f"Your guess is wrong. The number x is greater than {int(player_guess)}")

        elif generated_number<int(player_guess):
            print(f"Your guess is wrong. The number x is less than {int(player_guess)}")

        elif generated_number == int(player_guess):
            print(f"\nCongratulations! You guessed right! The number x is {generated_number}! Your competitive ranking is {points} points")
            break

        points-=50
        if points<=0:
            print("You got disqualified! Try again...")
            break
        player_guess = input("Try again: ")

else:
    print(f"Game mode under the name {game_mode} does not exist. Try again... ")


input("Press [Enter] to leave")


