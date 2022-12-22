filename = "advent3.txt"

def commonCh(sack):
    print(sack)
    commons = []
    for ch in sack[-1]:
        if sack[-2].count(ch) > 0:
            commons.append(ch)
    if len(sack) < 3: 
        print(commons)
        return commons[0]
    else: 
        print(commons, "commons")
        commons = "".join(commons)
        print(commons)
        sack.pop()
        sack.pop()
        sack.append(commons)
        print(sack)
        return commonCh(sack)

def points(ch):
    if ch >= 'A' and ch <= 'Z':
        return ord(ch) - ord('A') + 27
    else:
        return ord(ch) - ord('a') + 1

def splitEvenly(str, partitions):
    output = []
    partitionSize = len(str) // partitions
    for i in range(partitions):
        output.append(str[i * partitionSize: (i + 1) * partitionSize - 1])
    return output

def onlyAlphaN(str):
    return "".join([ch for ch in str if ch.isalnum()])

with open(filename) as f:
    sacks = f.readlines()
    print(sacks)
    #two sack solution
    # fun with list comprehension
    # takes each sack and splits it into two string in a list, while stripping out the \n
    sacks = [[sack[:half], "".join([ch for ch in sack[half:] if ch.isalnum()])] for sack, half in zip(sacks,[len(sack) // 2 for sack in sacks])]
    #print(sacks)

    common = [commonCh(sack) for sack in sacks]
    pointsList = [points(ch) for ch in common]

    #print(sum(pointsList))

    #part 2, three sack solution
    print("PART 2")
    sacks = [onlyAlphaN(sack) for sack in sacks]
    #split and zip list of sacks into lists of 3 sacks
    splitSacks = [sacks[::3], sacks[1::3], sacks[2::3]]
    zippedSacks = list(zip(splitSacks[0], splitSacks[1], splitSacks[2]))
    zippedSacks = [list(tup) for tup in zippedSacks]
    print(type(zippedSacks))
    commons = [commonCh(zippedSack) for zippedSack in zippedSacks]
    score = [points(ch) for ch in commons]
    print(sum(score))



