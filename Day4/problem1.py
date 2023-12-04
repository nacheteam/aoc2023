def parseInput(file):
    cont=1
    cards = {}
    for line in file:
        cleaned = line.strip()
        winning_numbers = cleaned.split('|')[0].strip().split(":")[1].strip().split(" ")
        owned_numbers = cleaned.split('|')[1].strip().split(" ")
        i = 0
        while i < len(winning_numbers):
            if winning_numbers[i] == "":
                winning_numbers.pop(i)
            else:
                i += 1
        i = 0
        while i < len(owned_numbers):
            if owned_numbers[i] == "":
                owned_numbers.pop(i)
            else:
                i += 1
        cards[cont] = [winning_numbers, owned_numbers]
        cont += 1
    return cards

def getPointsFromCard(card):
    points = 0
    for number in card[1]:
        if number in card[0]:
            points = 1 if points == 0 else points * 2
    return points

def getNumberOfWinnings(card):
    winnings = 0
    for number in card[1]:
        if number in card[0]:
            winnings += 1
    return winnings

def getPoints(cards):
    points = []
    for number, card in cards.items():
        points.append(getPointsFromCard(card))
    return points

def getTotalNumberOfCards(cards):
    # "number": [winning_numbers, owned_numbers, repetitions]
    copies = {}
    for number, card in cards.items():
        print(number, card)
        if number in copies.keys():
            print("Already in copies")
            numbers = [copies[number][0], copies[number][1]]
            w = getNumberOfWinnings(numbers)
            print("winnings: ", w)
            for j in range(copies[number][2]):
                for i in range(number+1, number+w+1):
                    copies[i] = [cards[i][0], cards[i][1], 1] if i not in copies.keys() else [copies[i][0], copies[i][1], copies[i][2]+1]
        print("Original")
        w = getNumberOfWinnings(card)
        print("winnings: ", w)
        for i in range(number+1, number+w+1):
            copies[i] = [cards[i][0], cards[i][1], 1] if i not in copies.keys() else [copies[i][0], copies[i][1], copies[i][2]+1]
    total = len(cards)
    for number, card in copies.items():
        total += card[2]
    return total

if __name__ == "__main__":
    file = open("input.txt", "r")
    cards = parseInput(file)
    points = getPoints(cards)
    print(points)
    print(sum(points))
    file.close()

    print(getTotalNumberOfCards(cards))