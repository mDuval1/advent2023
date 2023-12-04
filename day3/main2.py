from typing import Dict, List, Tuple


def get_star_adjacent_to_number(game, number, row, column):
    number_size = len(number)
    number_positions = [
        {"row": row, "column": c} for c in range(column, column + number_size)
    ]
    positions_to_check = []
    last_number_column = number_positions[-1]["column"]
    game_column_width = len(game[0])
    if row > 0:
        positions_to_check.extend(
            [{"row": n["row"] - 1, "column": n["column"]} for n in number_positions]
        )
        if column > 0:
            positions_to_check.append(
                {
                    "row": number_positions[0]["row"] - 1,
                    "column": number_positions[0]["column"] - 1,
                }
            )
        if last_number_column < game_column_width - 1:
            positions_to_check.append(
                {
                    "row": number_positions[-1]["row"] - 1,
                    "column": last_number_column + 1,
                }
            )
    if row < len(game) - 1:
        positions_to_check.extend(
            [{"row": n["row"] + 1, "column": n["column"]} for n in number_positions]
        )
        if column > 0:
            positions_to_check.append(
                {
                    "row": number_positions[0]["row"] + 1,
                    "column": number_positions[0]["column"] - 1,
                }
            )
        if last_number_column < game_column_width - 1:
            positions_to_check.append(
                {
                    "row": number_positions[-1]["row"] + 1,
                    "column": last_number_column + 1,
                }
            )
    if column > 0:
        positions_to_check.append({"row": row, "column": column - 1})
    if column < len(game[0]) - 1:
        positions_to_check.append({"row": row, "column": last_number_column + 1})
    for position in positions_to_check:
        if game[position["row"]][position["column"]] == "*":
            print(
                f"Row {row} has number {number} at position {column} adjacent to a star"
            )
            return {"row": position["row"], "column": position["column"]}
    return False


def main():
    with open("input.txt", "r") as f:
        input = f.read()
    game = input.split("\n")

    stars_adjacent_to_numbers: Dict[Tuple[int, int], List[int]] = {}
    for game_index, game_row in enumerate(game):
        current_number = ""
        current_number_position = -1
        for character_index, character in enumerate(game_row):
            if not character.isdigit():
                if current_number:
                    print(
                        f"Row {game_index} has number {current_number} at position {current_number_position}"
                    )

                    adjacent_numbers = get_star_adjacent_to_number(
                        game, current_number, game_index, current_number_position
                    )
                    if adjacent_numbers:
                        key = (adjacent_numbers["row"], adjacent_numbers["column"])
                        current_number_adjacent_to_star = stars_adjacent_to_numbers.get(
                            key, []
                        )
                        current_number_adjacent_to_star.append(int(current_number))
                        stars_adjacent_to_numbers[key] = current_number_adjacent_to_star

                    current_number = ""
                    current_number_position = -1
                continue
            if not current_number:
                current_number_position = character_index
            current_number += character
    total = 0
    print(stars_adjacent_to_numbers)
    for adjacent_numbers in stars_adjacent_to_numbers.values():
        if len(adjacent_numbers) == 2:
            total += adjacent_numbers[0] * adjacent_numbers[1]
    print(total)


if __name__ == "__main__":
    main()
