def efficient_part1():
    n = 1
    init_circle = 3018458
    while 2*n < init_circle:
        n = n*2
    print "The elf who takes all the presents is elf number ", (init_circle-n)*2+1
    
def efficient_part2():
    n = 2
    new_cycle = 4
    end_even = 3
    init_circle = 3018458
    while new_cycle+n*3 < init_circle:
        n = n*3
        new_cycle +=n
    pos_to_go = init_circle-new_cycle
    if new_cycle+n*3/2 <= init_circle:
        print "The elf who takes all the presents is elf number ", n*3/2+(init_circle-new_cycle-n*3/2)*2+2
    else:
        print "The elf who takes all the presents is elf number ", pos_to_go+1
     
efficient_part1()
efficient_part2()
