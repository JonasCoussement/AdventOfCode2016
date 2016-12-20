import re

instructions = open("Day12.txt").readlines()

def assembunny(inputs):
    registry = [0,0,0,0]
    if part2:
        registry[2] = 1
    registryindex = "abcd"
    i=0;
    while i < len(inputs):
        oper = inputs[i].split(' ',3)
        if oper[0] == "cpy":
            index1 = registryindex.find(oper[1])
            index2 = registryindex.find(oper[2].split("\n",1)[0])
            if index1 == -1:
                registry[index2] = int(oper[1])
            else:
                registry[index2] = registry[index1]
            i += 1
        elif oper[0] == "jnz":
            index1 = registryindex.find(oper[1])
            index2 = registryindex.find(oper[2].split("\n",1)[0])
            if index1 == -1:
                if int(oper[1]) > 0:
                    if index2 == -1:
                        i += int(oper[2])
                    else:
                        i += registry[index2]
                else:
                    i += 1
            else:
                if registry[index1] > 0:
                    if index2 == -1:
                        i += int(oper[2])
                    else:
                        i += registry[index2]
                else:
                    i += 1
        elif oper[0] == "inc":
            index1 = registryindex.find(oper[1].split("\n",1)[0])
            registry[index1] += 1
            i += 1
        elif oper[0] == "dec":
            index1 = registryindex.find(oper[1].split("\n",1)[0])
            registry[index1] -= 1
            i += 1
    print(registry)

part2 = False
assembunny(instructions)
part2 = True
assembunny(instructions)
