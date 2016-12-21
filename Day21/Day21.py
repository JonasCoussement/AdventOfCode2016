def get_instruct():
    instr = open("Day21.txt").readlines()
    return instr

def swap(instr):
    global password
    if instr[1] == "position":
        i = int(instr[2])
        j = int(instr[5])
    elif instr[1] == "letter":
        i = password.index(instr[2])
        j = password.index(instr[5])
    password[i], password[j] = password[j], password[i]
    return password

def rotate(instr):
    global password
    global part2
    if instr[1] == "based":
        move = password.index(instr[-1])
        if move >=4:
            move += 1
        move += 1
        if part2:
            cur_pos = password.index(instr[-1])
            if not cur_pos%2 == 0:
                move = (cur_pos+1)/2
            else:
                if cur_pos == 0:
                    move = 1
                elif cur_pos == 2:
                    move = -2
                elif cur_pos == 4:
                    move = -1
                else:
                    move = 0
    elif instr[1] == "right":
        move = int(instr[2])
    elif instr[1] == "left":
        move = -int(instr[2])
    move = move % len(password)
    if part2:
        move = -move
    return password[-move:] + password[:-move]

def reverse(instr):
    global password
    from_int = int(instr[2])
    to_int = int(instr[4])+1
    return password[0:from_int]+password[from_int:to_int][::-1]+password[to_int:]

def move(instr):
    global password
    global part2
    old_pos = int(instr[2])
    new_pos = int(instr[-1])
    if part2:
        old_pos,new_pos = new_pos,old_pos
    char = password[old_pos]
    del password[old_pos]
    password.insert(new_pos,char)
    return password
    
def decypher():
    global password
    global part2
    part2= False
    password = list("abcdefgh")
    instr = get_instruct()
    for i in range(0,len(instr)):
        instr_cur = instr[i].split(' ')
        instr_cur[-1] = instr_cur[-1].split('\n')[0]
        if instr_cur[0] == "swap":
            password = swap(instr_cur)
        elif instr_cur[0] == "rotate":
            password = rotate(instr_cur)
        elif instr_cur[0] == "reverse":
            password = reverse(instr_cur)
        elif instr_cur[0] == "move":
            password = move(instr_cur)
    print "The scrambled password is" , "".join(password)
    #part 2
    part2 = True
    password = list("fbgdceah")
    instr = get_instruct()[::-1]
    for i in range(0,len(instr)):
        instr_cur = instr[i].split(' ')
        instr_cur[-1] = instr_cur[-1].split('\n')[0]
        if instr_cur[0] == "swap":
            password = swap(instr_cur)
        elif instr_cur[0] == "rotate":
            password = rotate(instr_cur)
        elif instr_cur[0] == "reverse":
            password = reverse(instr_cur)
        elif instr_cur[0] == "move":
            password = move(instr_cur)
    print "The unscrambled password is" , "".join(password)
       
decypher()
