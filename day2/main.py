max_r = 12
max_g = 13
max_b = 14


def main():
    with open("input.txt", "r") as f:
        input = f.read()
    total = 0
    for game in input.split("\n"):
        round_problem = False
        game_info, rounds = game.split(":")
        game_id = int(game_info.split(" ")[1])
        for i, game_round in enumerate(rounds.split(";")):
            red = 0
            green = 0
            blue = 0
            for color in game_round.split(","):
                if "red" in color:
                    red += int(color.split(" red")[0])
                if "green" in color:
                    green += int(color.split(" green")[0])
                if "blue" in color:
                    blue += int(color.split(" blue")[0])
            if red > max_r or green > max_g or blue > max_b:
                round_problem = True
                break
        if not round_problem:
            print("Game {} has no problem".format(game_id))
            total += game_id
    print(total)


if __name__ == "__main__":
    main()
