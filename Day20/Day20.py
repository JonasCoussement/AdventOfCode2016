def blacklist():
    black = open("Day20.txt").readlines()
    for i in range(0,len(black)):
        black[i] = black[i].split('-',)
        black[i][0] = int(black[i][0])
        black[i][1] = int(black[i][1].split('\n',)[0])
    return black

def whitelist_part1():
    black_sort = sorted(blacklist())
    white = False
    check = 0
    black_index = 0
    while not white:
        if black_sort[black_index][0]<=check:
            check = max(check,black_sort[black_index][1])
            black_index += 1
        else:
            white = True
    print(check+1)
    
def whitelist_part2():
    black_sort = sorted(blacklist())
    white = 0
    check = 0
    black_index = 0
    while black_index<len(black_sort):
        if black_sort[black_index][0]<=check:
            check = max(check,black_sort[black_index][1])
            black_index += 1
        else:
            white += black_sort[black_index][0]-check-1
            check = black_sort[black_index][0]
    print(white)
    
whitelist_part1()
whitelist_part2()
