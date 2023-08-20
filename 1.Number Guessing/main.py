from random import randint

LOWER_NUM, HIGHER_NUM = 1, 15
NUMBER_OF_GUESSES = 3
WATCH_AD_LIMIT = 2


def generate_random_number():
    return randint(LOWER_NUM, HIGHER_NUM)


def get_extra_life(watch_ad_limit, random_num):
    invalid_flag = False

    while True:
        if watch_ad_limit != 0:
            not invalid_flag and print(f"Get extra life by watching ads - {watch_ad_limit} available")
            choice = input("\nDo you wish to watch ads(y/n)? ").lower()
            print("\n")
        else:
            print("No more ads available at the time\n")
            print(f"*** The random number was {random_num} ***")
            return 0, 0

        if choice == "y":
            number_of_guesses = 1
            watch_ad_limit = watch_ad_limit - 1
            return number_of_guesses, watch_ad_limit
        elif choice == "n":
            number_of_guesses = 0
            print(f"*** The random number was {random_num} ***\n")
            return number_of_guesses, watch_ad_limit
        else:
            print("You have entered an invalid option, please enter y/n only")
            invalid_flag = True


def play_guess_game():
    number_of_guesses = NUMBER_OF_GUESSES
    watch_ad_limit = WATCH_AD_LIMIT
    random_num = generate_random_number()

    while number_of_guesses > 0:
        try:
            user_guess: int = int(input("Guess: "))
            number_of_guesses = number_of_guesses - 1
        except ValueError:
            print("Please enter a valid number")
            continue

        if user_guess > random_num:
            print(f"The number is lower. You have {number_of_guesses} guesses left\n")
        elif user_guess < random_num:
            print(f"The number is greater. You have {number_of_guesses} guesses left\n")
        else:
            print("\nYou guessed it!!!\nYou won the game")
            break

        if number_of_guesses == 0:
            print(f"\n*** Game Over, you lost ***\n")
            number_of_guesses, watch_ad_limit = get_extra_life(watch_ad_limit, random_num)


if __name__ == "__main__":
    print(f'Guess the number in the range from {LOWER_NUM} to {HIGHER_NUM}\n')
    play_guess_game()