import random

overall_roll_entries = []


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def find_roll_distribution(result: list[int]) -> dict:
    roll_distribution = {}
    for value in result:
        if value in roll_distribution:
            roll_distribution[value] += 1
        else:
            roll_distribution[value] = 1
    return roll_distribution


def display_roll_distribution(roll_distribution: dict):
    print("\nRoll Value | Occurrence")
    for roll_value, occurrences in roll_distribution.items():
        print(f"{roll_value:^10} | {occurrences:^10}")


def get_stats(roll_entries: list[int]):
    total: int = sum(roll_entries)
    number_of_dice: int = len(roll_entries)
    average: float = total / number_of_dice

    roll_distribution: dict = find_roll_distribution(roll_entries)

    print("\n*** Roll Dice Stats ***\n")
    print(f"Total={total}\n")
    print(f"Average={average}")
    display_roll_distribution(roll_distribution)
    print("***********************\n")


def find_overall_roll_distribution():
    overall_distribution = {}  # This will store the overall roll distribution
    individual_distributions = []  # This will store individual roll distributions

    for roll_entry in overall_roll_entries:
        individual_distributions.append(find_roll_distribution(roll_entry))

    for individual_roll_entry in individual_distributions:
        for roll_value, occurrences in individual_roll_entry.items():
            if roll_value in overall_distribution:
                overall_distribution[roll_value] += occurrences
            else:
                overall_distribution[roll_value] = occurrences
    return overall_distribution


def save_roll_details(roll_entries: list[int]):
    overall_roll_entries.append(roll_entries)


def main():
    print('Type "exit" to end the program\n')
    while True:
        try:
            user_input: str = input("How many dice you want to roll: ")
            if user_input.lower() == "exit":
                print("\n***** Overall Roll Distribution *****")
                overall_distribution = find_overall_roll_distribution()
                display_roll_distribution(overall_distribution)
                print("\n*************************************")
                break
            roll_entries = roll_dice(int(user_input))
            print(*roll_entries, sep=",")
            save_roll_details(roll_entries)
            get_stats(roll_entries)
        except ValueError:
            print("Please enter a valid number or 'exit'\n")


if __name__ == "__main__":
    main()
