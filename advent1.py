open("hello.txt", 'a')
with open('advent1.txt') as f:
    lines = f.readlines()
    maxes = [0, 0, 0]
    current = 0
    for num in lines:
        if num == "\n":
            if current > min(maxes):
                maxes[maxes.index(min(maxes))] = current
            current = 0
        else:
            current += int(num)
    print(sum(maxes))

