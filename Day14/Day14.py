import hashlib
import re
import sys

sys.setrecursionlimit(3000)

def getKeys():
    inp = "yjdafjpo"
    noKeys = 0
    index = 0
    matcher3 = re.compile(r'(.)\1{2,}')
    matcher5 = re.compile(r'(.)\1{4,}')
    matched3 = []
    matched3Index = []
    keysIndex = []
    keys = []
    while noKeys<=64:
        hashcode = hashlib.md5(inp+str(index)).hexdigest()
        seq = re.findall(matcher3, hashcode)
        seq5 = re.findall(matcher5, hashcode)
        for i in range(0,len(seq5)):
            if seq5[i] in matched3:
                indices = [j for j, x in enumerate(matched3) if x == seq5[i]]
                for j in indices:
                    keysIndex.append(matched3Index[j])
                    keys.append(hashlib.md5(inp+str(matched3Index[j])).hexdigest())
                    noKeys+=1
                for j in reversed(indices):
                    del matched3[j]
                    del matched3Index[j]
        if len(seq) > 0:
            matched3.append(seq[0])
            matched3Index.append(index)
        index+=1
        if index>=1000:
            if matched3Index[0]<(index-1000):
                del matched3[0]
                del matched3Index[0]
    print("Search ended at index " + str(sorted(keysIndex)[63]) + " to generate 64 valid hashes")

getKeys()

def getHash(instring,stretch):
    if stretch<2017:
        return getHash(hashlib.md5(instring).hexdigest(),stretch+1)
    else:
        return instring

def getKeysStretched():
    inp = "yjdafjpo"
    noKeys = 0
    index = 0
    matcher3 = re.compile(r'(.)\1{2,}')
    matcher5 = re.compile(r'(.)\1{4,}')
    matched3 = []
    matched3Index = []
    keysIndex = []
    keys = []
    print("Searching for keys in stretched hashes")
    while noKeys<=64:
        hashcode = getHash(inp+str(index),0)
        seq = re.findall(matcher3, hashcode)
        seq5 = re.findall(matcher5, hashcode)
        for i in range(0,len(seq5)):
            if seq5[i] in matched3:
                indices = [j for j, x in enumerate(matched3) if x == seq5[i]]
                for j in indices:
                    keysIndex.append(matched3Index[j])
                    keys.append(hashlib.md5(inp+str(matched3Index[j])).hexdigest())
                    noKeys+=1
                    print("Key Found! number: " + str(noKeys))
                for j in reversed(indices):
                    del matched3[j]
                    del matched3Index[j]
        if len(seq) > 0:
            matched3.append(seq[0])
            matched3Index.append(index)
        index+=1
        if index>=1000:
            if matched3Index[0]<(index-1000):
                del matched3[0]
                del matched3Index[0]
    print(sorted(keysIndex)[63])

getKeysStretched()
