def parseInput(file):
    games = {}
    for line in file:
        line_clean = line.strip()
        game_id = int(line_clean.split(":")[0].split(" ")[1])
        game_rounds = line_clean.split(":")[1].split(";")
        cubes = {"red": 0, "blue": 0, "green": 0}
        for round in game_rounds:
            clean_round = round.strip()
            if "," in clean_round:
                shows = clean_round.split(", ")
                for show in shows:
                    clean_show = show.strip()
                    color = clean_show.split(" ")[1]
                    number = int(clean_show.split(" ")[0])
                    cubes[color] = max(cubes[color], number)
            else:
                color = clean_round.split(" ")[1]
                number = int(clean_round.split(" ")[0])
                cubes[color] = max(cubes[color], number)
        games[game_id] = cubes
    return games

def possibleGames(games, red, blue, green):
    possible_games_ids = []
    for game_id, cubes in games.items():
        if cubes["red"] <= red and cubes["blue"] <= blue and cubes["green"] <= green:
            print("Game ", game_id, " is possible")
            print("Red: ", cubes["red"], " Blue: ", cubes["blue"], " Green: ", cubes["green"])
            possible_games_ids.append(game_id)
    return possible_games_ids

def findPower(games):
    powers = []
    for game_id, cubes in games.items():
        power = cubes["red"] * cubes["blue"] * cubes["green"]
        powers.append(power)
    return powers

if __name__ == "__main__":
    file = open("input1.txt", "r")
    games = parseInput(file)
    file.close()

    red = 12
    blue = 14
    green = 13

    possible_games_ids = possibleGames(games, red, blue, green)
    print("Possible games: ", possible_games_ids)
    sum_of_possible_games = sum(possible_games_ids)
    print("Sum of possible games: ", sum_of_possible_games)

    powers = findPower(games)
    print("Powers: ", powers)
    sum_of_powers = sum(powers) 
    print("Sum of powers: ", sum_of_powers)