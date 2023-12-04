def main():
    with open("input.txt", "r") as f:
        input = f.read()
    total = 0
    for game in input.split("\n"):
        game_info, rounds = game.split(":")
        game_id = int(game_info.split(" ")[1])
        min_red = 0
        min_green = 0
        min_blue = 0
        for i, game_round in enumerate(rounds.split(";")):
            for color in game_round.split(","):
                if "red" in color:
                    red = int(color.split(" red")[0])
                    if red > min_red:
                        min_red = red
                if "green" in color:
                    green = int(color.split(" green")[0])
                    if green > min_green:
                        min_green = green
                if "blue" in color:
                    blue = int(color.split(" blue")[0])
                    if blue > min_blue:
                        min_blue = blue
        game_power = min_red * min_green * min_blue
        print("Game {} has power {}".format(game_id, game_power))
        total += game_power
    print(total)


if __name__ == "__main__":
    main()
