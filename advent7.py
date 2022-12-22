


class Dir:
    def __init__(self, parent, root):
        self.size = 0
        self.subs = {}
        self.parent = parent
        self.root = root

    def updateAllSizes(self):
        for subDir in self.subs.values():
            self.size += subDir.updateAllSizes()
        return self.size

    def sizeOfAllDirs(self):
        size = [self.size]
        for subDir in self.subs.values():
            size += subDir.sizeOfAllDirs()
        return size

    def addDir(self, name):
        self.subs[name] = Dir(self, self.root)

    def addSize(self, size):
        self.size += size



filename = "advent7.txt"

with open(filename) as f:
    #reminder: Mutables in Python are passed by reference
    root = Dir(None, None)
    root.root = root
    curDir = root
    lines = f.readlines()
    readingls = False
    for command in [line.split() for line in lines]:
        if readingls:
            if command[0] == "dir":
                curDir.addDir(command[1])
            elif command[0].isnumeric():
                curDir.addSize(int(command[0]))
            else:
                readingls = False
        if command[0] == "$":
            if command[1] == "ls":
                readingls = True
            if command[1] == "cd":
                if command[2] == "/":
                    curDir = root
                elif command[2] == "..":
                    curDir = curDir.parent
                    if curDir == None:
                        Exception("root does not have a parent dir")
                else:
                    curDir = curDir.subs[command[2]]
        else:
            Exception("weird, something went wrong")
    root.updateAllSizes()

    totalDiskSize = 70000000
    spaceNeeded = 30000000
    spaceUsed = root.size
    extraSpaceRequired = spaceUsed - (totalDiskSize - spaceNeeded)


    print(sum([size for size in root.sizeOfAllDirs() if size <= 100000]))
    print(min([size for size in root.sizeOfAllDirs() if size >= extraSpaceRequired]))

    print(root.sizeOfAllDirs())







