import re

def botlist(commands):
    #generate a list of bots from the instructions
    maxbot = 0
    for i in range(0,len(commands)):
        if re.match("bot", commands[i]):
            bots = [e for e in re.split("[^0-9+]", commands[i]) if e != '']
            maxbotno = max(map(int, bots))
            if maxbotno > maxbot:
                maxbot = maxbotno
    botslist = []
    for i in range(0,maxbot+1):
        botslist.append([-1,-1])
    return botslist

def command(instruct):
    botslist = botlist(instruct)
    #run through instructions
    #execute and remove commands until bot receives 2 chips
    #start instruction list from top
    i = 0
    outputs = [0]*250
    while i<len(instruct):
        #if redistribution command
        if re.match("bot", instruct[i]):
            botno = [e for e in re.split("[^0-9+]", instruct[i]) if e != '']
            bot0 = int(botno[0])
            bot1 = int(botno[1])
            bot2 = int(botno[2])
            #check if bot has 2 chips
            if botslist[bot0][0]>0 and botslist[bot0][1]>0:
                #redistribute chips
                #check if one or more chips go to output
                output = instruct[i].find("output")
                bot = instruct[i][4:].find("bot")
                #execute and remove command
                instruct[i] = "executed"
                chip1 = True
                chip2 = True
                if output>0:
                    if bot == -1:
                        outputs[int(botno[1])] = botslist[bot0][0]
                        outputs[int(botno[2])] = botslist[bot0][1]
                        botslist[bot0][0] = -1
                        botslist[bot0][1] = -1
                        chip1 = False
                        chip2 = False
                    else:
                        if bot>output:
                            outputs[int(botno[1])] = botslist[bot0][0]
                            botslist[bot0][0] = -1
                            chip1 = False
                        else:
                            outputs[int(botno[2])] = botslist[bot0][1]
                            botslist[bot0][1] = -1
                            chip2 = False
                #check if new bot already has chip
                if botslist[bot1][0]>0 and chip1 == True:
                    #is new chip of higher value?
                    if botslist[bot1][0]<botslist[bot0][0]:
                        botslist[bot1][1] = botslist[bot0][0]
                        botslist[bot0][0] = -1
                    else:
                        botslist[bot1][1] = botslist[bot1][0]
                        botslist[bot1][0] = botslist[bot0][0]
                        botslist[bot0][0] = -1
                    #new bot with 2 chips rerun list of command
                    i = 0
                elif chip1 == True:
                    botslist[bot1][0] = botslist[bot0][0]
                    botslist[bot0][0] = -1
                    i+=1
                if botslist[bot2][0]>0 and chip2 == True:
                    if botslist[bot2][0]<botslist[bot0][1]:
                        botslist[bot2][1] = botslist[bot0][1]
                        botslist[bot0][0] = -1
                    else:
                        botslist[bot2][1] = botslist[bot2][0]
                        botslist[bot2][0] = botslist[bot0][1]
                        botslist[bot0][1] = -1
                    #new bot with 2 chips rerun list of command
                    i = 0
                elif chip2 == True:
                    botslist[bot2][0] = botslist[bot0][1]
                    botslist[bot0][1] = -1
            else:
                i +=1
        elif re.match("value", instruct[i]):
            inputs = [e for e in re.split("[^0-9+]", instruct[i]) if e != '']
            #execute and remove command
            instruct[i] = "executed"
            chipno = int(inputs[0])
            botno = int(inputs[1])
            #check if new bot already has chip
            if botslist[botno][0]>0:
                #is new chip of higher value?
                if botslist[botno][0]<chipno:
                    botslist[botno][1] = chipno
                else:
                    botslist[botno][1] = botslist[botno][0]
                    botslist[botno][0] = chipno
                #new bot with 2 chips rerun list of command
                i = 0
            else:
                botslist[botno][0] = chipno
                i+=1
        elif re.match("executed", instruct[i]):
            i+=1
        if part1:
            #check list of bots which has 61 and 17
            for j in range(0,len(botslist)):
                if botslist[j][0] == 17 and botslist[j][1] == 61:
                    print("bot responsible for comparing 17 and 61:")
                    print(j)
                    i = len(instruct)
    if not part1:
        print(outputs[0]*outputs[1]*outputs[2])
    
instructions = open("Day10.txt").readlines()
part1=True
command(instructions)
instructions = open("Day10.txt").readlines()
part1=False
command(instructions)
