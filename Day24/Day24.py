import itertools

def init_grid():
    grid = open("Day24.txt").readlines()
    for i in range(len(grid)):
        grid[i] = grid[i].split("\n")[0]
    return list(grid)

def get_pos_perm(grid):
    nodes_to_pass = 0
    coord_of_numbers = range(0,8)
    for i in range(len(grid)):
        number = [int(s) for s in grid[i].split()[0] if s.isdigit()]
        if len(number) > 0:
            for j in range(0,len(number)):
                coord_of_numbers[int(number[j])] = [i,grid[i].split()[0].find(str(number[j]))]
            if max(number) > nodes_to_pass:
                nodes_to_pass = max(number)
    perms = list(itertools.permutations(range(1,nodes_to_pass+1)))
    perms2 = list(itertools.permutations(range(0,nodes_to_pass+1),2))
    return coord_of_numbers,perms, perms2

def openspace(x,y):
    global grid
    if grid[x][y] != "#":
        return True
    else:
        return False
    
def step(xy):
    global grid
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
    return steps

def find_path(part):
    global grid
    grid = init_grid()
    coord_of_numbers, pos_paths, pos_connec = get_pos_perm(grid)
    short_path_connec = []
    for i in range(0,len(pos_connec)):
        start = coord_of_numbers[pos_connec[i][0]]
        stop = coord_of_numbers[pos_connec[i][1]]
        short_path_connec.append(path(start,stop))
    path_length = []
    shortest_path = 50000
    #print pos_connec
    #print short_path_connec
    for i in range(len(pos_paths)):
        path_len = short_path_connec[pos_connec.index((0,pos_paths[i][0]))]
        for j in range(1,len(pos_paths[i])):
            path_len += short_path_connec[pos_connec.index((pos_paths[i][j-1],pos_paths[i][j]))]
        if part:
            path_len += short_path_connec[pos_connec.index((0,pos_paths[i][-1]))]
        path_length.append(path_len)
        if path_len < shortest_path:
            shortest_path = path_len 
    print min(path_length)

part2 = False
find_path(part2)
part2 = True
find_path(part2)
