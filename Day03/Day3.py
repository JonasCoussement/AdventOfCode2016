import os
import re

os.chdir("C:/Users/User/Documents/AdventOfCode")
with open("Day3.txt") as f:
    content = f.readlines()

success = 0
for x in range(0, len(content)):
    #extract all numbers
    triangle = [int(s) for s in re.findall(r'\d+',content[x])]
    sort = sorted(triangle)
    if (sort[0]+sort[1]>sort[2]):
        success = success+1
                
print(success)

#part2
success = 0
for x in range(0, int(len(content)/3)):
    #extract all numbers
    dummy1 = [int(s) for s in re.findall(r'\d+',content[x*3])]
    dummy2 = [int(s) for s in re.findall(r'\d+',content[x*3+1])]
    dummy3 = [int(s) for s in re.findall(r'\d+',content[x*3+2])]
    triangle1 = sorted([dummy1[0],dummy2[0],dummy3[0]])
    triangle2 = sorted([dummy1[1],dummy2[1],dummy3[1]])
    triangle3 = sorted([dummy1[2],dummy2[2],dummy3[2]])
    if (triangle1[0]+triangle1[1]>triangle1[2]):
        success = success+1
    if (triangle2[0]+triangle2[1]>triangle2[2]):
        success = success+1
    if (triangle3[0]+triangle3[1]>triangle3[2]):
        success = success+1
                
print(success)
