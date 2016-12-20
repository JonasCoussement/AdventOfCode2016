import re

content = open("Day9.txt").readlines()[0]

pattern = re.compile('\(\d+x\d+\)')
def unzip(string):
    length = 0
    while len(string)>0:
        patternmatch = pattern.search(string)
        if not patternmatch:
            length += len(string)
            string = []
        elif patternmatch.span()[0] > 0:
            length += patternmatch.span()[0]
            string = string[patternmatch.span()[0]:]
        elif pattern.match(string):
            charstocopy= re.compile('\(\d+').match(string).group(0)[1:]
            copytimes = re.compile('\(\d+x\d+').match(string).group(0)[(2+len(charstocopy)):]
            instructlen = len(charstocopy)+len(copytimes)+3
            if part2:
                length += int(unzip(string[instructlen:(instructlen+int(charstocopy))]))*int(copytimes)
            else:
                length += int(charstocopy)*int(copytimes)
            string = string[(instructlen+int(charstocopy)):]
    return length

part2 = False
print(unzip(content))
part2 = True
print(unzip(content)) 
