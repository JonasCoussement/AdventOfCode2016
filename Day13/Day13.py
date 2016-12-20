def openspace(x,y):
    no = 1350
    system = x*x+3*x+2*x*y+y+y*y+no
    binar = bin(system).count("1")
    if binar % 2 == 0:
        return True
    else:
        return False

def step(xy):
    global length
    for i in [-1,1]:
        xnext = xy[0]+i
        ynext = xy[1]
        if xnext >= 0 and ynext >= 0 and openspace(xnext,ynext):
            if not [xnext,ynext] in visited:
                visited.append([xnext,ynext])
                length += [steps+1]
        else:
            wall.append([xnext,ynext])
        xnext = xy[0]
        ynext = xy[1]+i
        if xnext >= 0 and ynext >= 0 and openspace(xnext,ynext):
            if not [xnext,ynext] in visited:
                visited.append([xnext,ynext])
                length += [steps+1]
        else:
            wall.append([xnext,ynext])

def path(start,stop):
    global visited
    global wall
    global length
    global steps
    steps = 0
    length = [0]
    visited = [start]
    wall = []
    while not stop in visited:
        curstep = length.index(steps)
        curvisited = visited[:]
        for i in range(1,len(length)-curstep+1):
            step(curvisited[-i])
        steps+=1
        if steps == 50:
            print("Total number of places visited after 50 steps: " + str(len(visited)))
    print("Steps required to reach [31,39]: " + str(steps))

path([1,1],[31,39])
    
import matplotlib.pyplot as plt
plt.scatter([x[0] for x in visited],[x[1] for x in visited],marker='.')
plt.scatter([x[0] for x in wall],[x[1] for x in wall],color='red',marker='x')
plt.scatter([1,31],[1,39],color='green')
plt.show()
