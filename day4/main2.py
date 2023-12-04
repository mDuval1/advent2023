def main():
    with open("input.txt", "r") as f:
        input = f.read()
    cards = input.split("\n")
    total = 0
    card_to_copies_count = {i + 1: 1 for i in range(0, len(cards))}
    for card in cards:
        card_id, card_details = card.split(":")
        card_number = int(card_id.split("Card")[1].strip())
        current_copies_count = card_to_copies_count[card_number]
        print(card_to_copies_count, current_copies_count, card_number)
        winning_numbers, numbers_in_hand = card_details.split("|")
        winning_numbers = list(filter(lambda x: x != "", winning_numbers.split(" ")))
        numbers_in_hand = list(filter(lambda x: x != "", numbers_in_hand.split(" ")))
        set_of_winning_numbers = set(winning_numbers)
        winning_numbers_in_hand = 0
        for number in numbers_in_hand:
            if number in set_of_winning_numbers:
                winning_numbers_in_hand += 1

        if winning_numbers_in_hand > 0:
            print(f"Card {card_number} has {winning_numbers_in_hand} winning numbers")
            for i in range(1, winning_numbers_in_hand + 1):
                card_to_copies_count[card_number + i] += current_copies_count
    print(f"Final copies count: {card_to_copies_count}")
    total = sum(card_to_copies_count.values())
    print("Total number of scratchcards is {}".format(total))


if __name__ == "__main__":
    main()
