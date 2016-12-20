def getSetup():
    raw = open("Day15.txt").readlines()
    no_pos = []
    start_pos = []
    for i in range(0,len(raw)):
        raw_split = raw[i].split(" ")
        no_pos.append(int(raw_split[3]))
        start_pos.append(int(raw_split[-1][:-2]))
    return no_pos, start_pos

def part2(no_pos,start_pos):
    no_pos.append(11)
    start_pos.append(0)
    return no_pos, start_pos
    
def activateMachine():
    no_pos, start_pos = getSetup()
    time = 0
    while True:
        for i in range(0,len(start_pos)):
            cur_pos = (start_pos[i]+1+i+time)%no_pos[i]
            if cur_pos > 0:
                break
        else:
            break
        time += 1
    print("The first time you can catch a capsule is at t = " + str(time))
    no_pos, start_pos = part2(no_pos, start_pos)
    time = 0
    while True:
        for i in range(0,len(start_pos)):
            cur_pos = (start_pos[i]+1+i+time)%no_pos[i]
            if cur_pos > 0:
                break
        else:
            break
        time += 1
    print("With the new configuration, the first time you can catch a capsule is at t = " + str(time))
            
activateMachine()
