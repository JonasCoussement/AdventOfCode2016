import hashlib

def calc_path(path):
    global puz_inp
    global doors
    open_doors = []
    hashcode = hashlib.md5(puz_inp+path).hexdigest()[0:4]
    for i in range(0,4):
        if hashcode[i] in doors:
            open_doors.append(True)
        else:
            open_doors.append(False)
    return open_doors

def main():
    global puz_inp
    global doors
    prev_pos = [[0,0]]
    puz_inp = "pxxbnzuo"
    doors = "bcdef"
    prev_path = [""]
    final_pos = [3,3]
    max_steps = 0
    steps = 0
    while len(prev_pos)>0:
        steps += 1
        cur_pos = []
        cur_path = []
        for i in range(0,len(prev_path)):
            open_doors = calc_path(prev_path[i])
            if True in open_doors:
                for j in range(0,len(open_doors)):
                    if open_doors[j]:
                        if j == 0 and prev_pos[i][0] > 0:
                           cur_pos.append([prev_pos[i][0]-1,prev_pos[i][1]])
                           cur_path.append(prev_path[i]+"U")
                        elif j == 1 and prev_pos[i][0] < 3:
                           cur_pos.append([prev_pos[i][0]+1,prev_pos[i][1]])
                           cur_path.append(prev_path[i]+"D")
                        elif j == 2 and prev_pos[i][1] > 0:
                           cur_pos.append([prev_pos[i][0],prev_pos[i][1]-1])
                           cur_path.append(prev_path[i]+"L")
                        elif j == 3 and prev_pos[i][1] < 3:
                           cur_pos.append([prev_pos[i][0],prev_pos[i][1]+1])
                           cur_path.append(prev_path[i]+"R")
        prev_pos = cur_pos[:]
        prev_path = cur_path[:]
        while final_pos in prev_pos:
            if max_steps == 0:
                print("The shortest path to the vault is: " + str(prev_path[prev_pos.index([3,3])]))
            max_steps = steps
            del prev_path[prev_pos.index([3,3])]
            del prev_pos[prev_pos.index([3,3])]
    print("The maximum amount of steps that can be taken to reach the vault is : " + str(max_steps))

main()
