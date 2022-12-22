

class Valve:

    def __init__(self, flow = 0):
        self.flow = flow
        self.tunnels = {}
        self.open = False


    def getTunnel(self, name):
        return self.tunnels[name][0]

    def getDistance(self, name):
        return self.tunnels[name][1]


    def print(self, name):
        print("Valve " + name + " has flow rate=" + str(self.flow) + "; tunnels lead to valves " + str(self.tunnels))

    def addTunnel(self, name, valve, distance):
        if (not name in self.tunnels) and valves[name] != self:
            self.tunnels[name] = [valve, distance]

    def transferTunnels(self, tunnelName, distance):
        #assume tunnelName is a string that is a key in self.tunnels with a distance of distance
        transferor = self.getTunnel(tunnelName)
        for tunnel in self.getTunnel(tunnelName).tunnels:
            self.addTunnel(tunnel, transferor.tunnels[tunnel][0], transferor.tunnels[tunnel][1] + distance)
        self.tunnels.pop(tunnelName)


    def simplifyTunnels(self, origin):
        simplified = True
        names = (self.tunnels.keys())
        names = list(names).copy()
        for name in names:
            if self.getTunnel(name).flow == 0:
                simplified = False
                self.transferTunnels(name, self.getDistance(name))
        return simplified

    def maxVol(self, time):
        if time == 25:
            print("maxVol at ", time)
        if time < 0: return 0
        #problem: repeated valves
        isAlreadyOpen = self.open
        if self.open:
            currentValveFlow = 0
        else:
            self.open = True
            currentValveFlow = (self.flow * (time - 1))
        maxTunnelVol = 0
        for tunnel in self.tunnels:
            tunnelMax = self.getTunnel(tunnel).maxVol(time - self.getDistance(tunnel))
            maxTunnelVol = max(maxTunnelVol, tunnelMax)
        if not isAlreadyOpen:
            self.open = False
        return maxTunnelVol + currentValveFlow

    def bestPath(self, time):
        if time < 0: return [""]
        if time == 0: return [self]
        bestPath = []
        bestVol = 0
        for tunnel in self.tunnels:
            path = self.getTunnel(tunnel).bestPath(time - self.getDistance(tunnel))
            vol = volume(path)
            if vol > bestVol:
                return True

        return bestPath

def volume(path, time):
    counter = 0
    openedValves = []
    for valve, next in zip(path[:-1], path[1:]):
        print(valve, time)
        if not valves[valve].open and valves[valve].flow > 0:
            print("opening")
            time -= 1
            valves[valve].open = True
            openedValves.append(valve)
            counter += valves[valve].flow * time
            print(counter)
        print(time)
        print(valves[valve].getDistance(next))
        time -= valves[valve].getDistance(next)
        print(time)
    valve = path[-1]
    if not valves[valve].open:
        time -= 1
        valves[valve].open = True
        openedValves.append(valve)
        counter += valves[valve].flow * time
        print(valve, time)
    for valve in openedValves:
        valves[valve].open = False
    return counter

filename = "advent16.txt"
with open(filename) as f:
    lines = f.readlines()
    splitLines = [line.split() for line in lines]
    valves = {}
    #create valves
    for sLine in splitLines:
        valves[sLine[1]] = Valve(int(sLine[4][5:-1]))
    #create tunnels
    for sLine in splitLines:
        tunnels = sLine[9:]
        for tunnel in tunnels:
            #remove comma
            print(tunnel)
            tunnel = "".join([ch for ch in tunnel if ch.isalpha()])
            valves[sLine[1]].addTunnel(tunnel, valves[tunnel], 1)
    for valve in valves:
        valves[valve].print(valve)
    print("\n\nsimplifying\n\n")
    valves["AA"].simplifyTunnels("AA")
    complete = False
    while not complete:
        complete = True
        for valve in valves:
            simplified = valves[valve].simplifyTunnels(valve)
            if not simplified:
                complete = False

    for valve in valves:
        valves[valve].print(valve)

    print(volume(["AA", "DD", "BB", "JJ"], 10))
    print("\n\n\n", valves["AA"].maxVol(25))
