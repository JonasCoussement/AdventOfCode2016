import time

def getinitialsetup(filename):
    setup = open(filename).readlines()
    generators = []
    generatorpos = []
    microchips = []
    microchippos = []
    for i in range(0,len(setup)):
        floor = setup[i].split(' ')
        for j in range(0,len(floor)):
            if floor[j].find("generator") == 0:
                generators.append(floor[j-1])
                generatorpos.append(i+1)
            elif floor[j].find("microchip") == 0:
                microchips.append(floor[j-1])
                microchippos.append(i+1)
    #order of microchips and generators is identical
    elevator = 1
    return elevator,generatorpos,microchippos

def movelegality(generatorpos,microchippos):
    condition = []
    for i in range(0,len(generatorpos)):
        #if microchip is on same floor as it's generator
        if microchippos[i]==generatorpos[i]:
            condition.append(True)
        #if microchip is not on the same floor as any generator
        elif not microchippos[i] in generatorpos:
            condition.append(True)
        else:
            condition.append(False)
            break
    if False in condition:
        return False
    else:
        return True

def pairpositions(elevator,generatorpos,microchippos):
    #chip and generator pairs are interchangeable
    global length
    global steps
    pairs = sorted(zip(generatorpos,microchippos))
    if not [elevator]+pairs in visited:
        visited.append([elevator]+pairs)
        length.append(steps+1)

def move(position):
    global visited
    global length
    global steps
    elevator = position[0]
    generatorpos = [x[0] for x in position[1:]]
    microchippos = [x[1] for x in position[1:]]
    move2 = False
    if elevator == 1:
        moved = [1]
    elif elevator == 4:
        moved = [-1]
    elif elevator ==2:
        #check if floor 1 is not empty
        floor1 = 1 in generatorpos or 1 in microchippos
        if not floor1:
            moved = [1]
        else:
            moved = [1,-1]
    elif elevator ==3:
        floor1 = 1 in generatorpos or 1 in microchippos
        floor2 = 2 in generatorpos or 2 in microchippos
        if floor1 or floor2:
            moved = [1,-1]
        else:
            moved = [1]
        floor4 = 4 in generatorpos or 4 in microchippos
        if not floor4:
            move2 = True
    for k in moved:
        newelevator = elevator
        newelevator +=k
        generonfloor = [i for i, x in enumerate(generatorpos) if x == elevator]
        chipsonfloor = [i for i, x in enumerate(microchippos) if x == elevator]
        for i in range(0,len(generonfloor)):
            for j in range(0,len(chipsonfloor)):
                newgener = generatorpos[:]
                newgener[generonfloor[i]]+=k
                newmicro = microchippos[:]
                newmicro[chipsonfloor[j]]+=k
                if movelegality(newgener,newmicro):
                    pairpositions(newelevator,newgener,newmicro)                    
        if len(generonfloor)>1:
            for i in range(0,len(generonfloor)):
                for j in range(0,len(generonfloor)):
                    if not i == j:
                        newgener = generatorpos[:]
                        newgener[generonfloor[i]]+=k
                        newgener[generonfloor[j]]+=k
                        if movelegality(newgener,microchippos):
                            pairpositions(newelevator,newgener,microchippos)
        if len(chipsonfloor)>1:
            for i in range(0,len(chipsonfloor)):
                for j in range(0,len(chipsonfloor)):
                    if not i == j:
                        newmicro = microchippos[:]
                        newmicro[chipsonfloor[i]]+=k
                        newmicro[chipsonfloor[j]]+=k
                        if movelegality(generatorpos,newmicro):
                            pairpositions(newelevator,generatorpos,newmicro)
        if not move2:
            for i in range(0,len(generonfloor)):
                newgener = generatorpos[:]
                newgener[generonfloor[i]]+=k
                if movelegality(newgener,microchippos):
                    pairpositions(newelevator,newgener,microchippos)
            for i in range(0,len(chipsonfloor)):
                newmicro = microchippos[:]
                newmicro[chipsonfloor[i]]+=k
                if movelegality(generatorpos,newmicro):
                    pairpositions(newelevator,generatorpos,newmicro)
                 
                
    
def main(filename):
    elevator,generatorpos,microchippos = getinitialsetup(filename)
    global visited
    global steps
    global length
    steps = 0
    length = [0]
    visited = [[elevator] + sorted(zip(generatorpos,microchippos))]
    allontop = [4]+sorted(zip([4]*len(generatorpos),[4]*len(generatorpos)))
    while not allontop in visited:
        newsteps = visited[:]
        curstep = length.index(steps)
        for i in range(1,len(length)-curstep+1):
            move(newsteps[-i])
        steps+=1
        print(steps)
    print("solution found after: " + str(steps) + " steps")

filename = "Day11.txt"
main(filename)
filename = "Day11b.txt"
main(filename)
