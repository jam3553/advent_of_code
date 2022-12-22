from os import curdir

draw = 0
lose = 1
win = 2

def points(chA, chB):
    winPoints = 0
    a = ord(chA) - ord('A') + 1
    b = ord(chB) - ord('X') + 1
    

    if (b - a) % 3 == 1:
        winPoints = 6
    if (b - a) % 3 == 0:
        winPoints = 3
    return winPoints + b

def move(chA, chB):
    a = ord(chA) - ord('A')
    b = ord(chB) - ord('X') - 1

    print(chA, chB, (a + b) % 3, chr((a + b) % 3 + ord('X')))
    return chr((a + b) % 3 + ord('X'))


filename = "advent2.txt"

print(filename)

with open(filename) as f:
    games = f.readlines()
    games = [game.split() for game in games]
    print(games)

    totalPoints = 0
    points2 = 0
    for game in games:
        totalPoints += points(game[0], game[1])
        points2 += points(game[0], move(game[0], game[1]))
    print(totalPoints)
    print(points2)

