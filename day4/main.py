def main():
    with open("input.txt", "r") as f:
        input = f.read()
    cards = input.split("\n")
    total = 0
    for card in cards:
        card_id, card_details = card.split(":")
        card_number = card_id.split(" ")[1]
        winning_numbers, numbers_in_hand = card_details.split("|")
        winning_numbers = list(filter(lambda x: x != "", winning_numbers.split(" ")))
        numbers_in_hand = list(filter(lambda x: x != "", numbers_in_hand.split(" ")))
        print(
            f"Card {card_number} has numbers {numbers_in_hand}, winning numbers are {winning_numbers}"
        )
        set_of_winning_numbers = set(winning_numbers)
        winning_numbers_in_hand = 0
        for number in numbers_in_hand:
            if number in set_of_winning_numbers:
                winning_numbers_in_hand += 1
        if winning_numbers_in_hand > 0:
            print(f"Card {card_number} has {winning_numbers_in_hand} winning numbers")
            total += 2 ** (winning_numbers_in_hand - 1)
        else:
            print(f"Card {card_number} has no winning numbers")
    print(total)


if __name__ == "__main__":
    main()
