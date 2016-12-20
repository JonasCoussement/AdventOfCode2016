def initial():
    puzzleinput = "00111101111101000"
    disclength = 272
    return puzzleinput, disclength

def checksum(string):
    check = []
    for i,k in zip(string[0::2], string[1::2]):
        if i == k:
            check.append('1')
        else:
            check.append('0')
    print 'checksum length: ', len(check)
    if len(check)%2 == 0:
        return checksum(check)
    else:
        return "".join(check)

def generateDragon(string):
    global disclength
    a = string[:]
    b = a[::-1]
    b = b.replace('1','2')
    b = b.replace('0','1')
    b = b.replace('2','0')
    result = a+str(0)+b
    if len(result)<disclength:
        return generateDragon(result)
    else:
        return result

def main():
    global disclength
    puzzleinput, disclength = initial()
    result = generateDragon(puzzleinput)
    check = checksum(result[:disclength])
    print 'Resulting data string for part 1:',result
    print 'With complementary checksum', check
    disclength = 35651584
    result = generateDragon(puzzleinput)
    check = checksum(result[:disclength])
    print
    print 'Checksum for part 2:', check
main()
