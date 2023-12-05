import sys
def isDigit(s, i):
    if s[i]>='0' and s[i]<='9':
        return True
    elif (s[i]=='o' or s[i]=='O') and i+2<len(s):
        if s[i+1]=='n' or s[i+1]=='N':
            if s[i+2]=='e' or s[i+2]=='E':
                return True
        return False
    elif (s[i]=='t' or s[i]=='T') and i+2<len(s):
        if s[i+1]=='w' or s[i+1]=='W':
            if s[i+2]=='o' or s[i+2]=='O':
                return True
        elif (s[i+1]=='h' or s[i+1]=='H') and i+3<len(s):
            if s[i+2]=='r' or s[i+2]=='R':
                if s[i+3]=='e' or s[i+3]=='E':
                    return True
        return False
    elif (s[i]=='f' or s[i]=='F') and i+3<len(s):
        if s[i+1]=='o' or s[i+1]=='O':
            if s[i+2]=='u' or s[i+2]=='U':
                if s[i+3]=='r' or s[i+3]=='R':
                    return True
        elif s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='v' or s[i+2]=='V':
                if s[i+3]=='e' or s[i+3]=='E':
                    return True
        return False
    elif (s[i]=='s' or s[i]=='S') and i+2<len(s):
        if s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='x' or s[i+2]=='X':
                return True
        elif (s[i+1]=='e' or s[i+1]=='E') and i+4<len(s):
            if s[i+2]=='v' or s[i+2]=='V':
                if s[i+3]=='e' or s[i+3]=='E':
                    if s[i+4]=='n' or s[i+4]=='N':
                        return True
        return False
    elif (s[i]=='e' or s[i]=='E') and i+4<len(s):
        if s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='g' or s[i+2]=='G':
                if s[i+3]=='h' or s[i+3]=='H':
                    if s[i+4]=='t' or s[i+4]=='T':
                        return True
        return False
    elif (s[i]=='n' or s[i]=='N') and i+3<len(s):
        if s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='n' or s[i+2]=='N':
                if s[i+3]=='e' or s[i+3]=='E':
                    return True
        return False
    
    else:
        return False
def getDigit(s, i):
    if s[i]>='0' and s[i]<='9':
        return int(s[i])
    elif s[i]=='o' or s[i]=='O':
        if s[i+1]=='n' or s[i+1]=='N':
            if s[i+2]=='e' or s[i+2]=='E':
                return 1
        return 0
    elif s[i]=='t' or s[i]=='T':
        if s[i+1]=='w' or s[i+1]=='W':
            if s[i+2]=='o' or s[i+2]=='O':
                return 2
        elif s[i+1]=='h' or s[i+1]=='H':
            if s[i+2]=='r' or s[i+2]=='R':
                if s[i+3]=='e' or s[i+3]=='E':
                    return 3
        return 0
    elif s[i]=='f' or s[i]=='F':
        if s[i+1]=='o' or s[i+1]=='O':
            if s[i+2]=='u' or s[i+2]=='U':
                if s[i+3]=='r' or s[i+3]=='R':
                    return 4
        elif s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='v' or s[i+2]=='V':
                if s[i+3]=='e' or s[i+3]=='E':
                    return 5
        return 0
    elif s[i]=='s' or s[i]=='S':
        if s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='x' or s[i+2]=='X':
                return 6
        elif s[i+1]=='e' or s[i+1]=='E':
            if s[i+2]=='v' or s[i+2]=='V':
                if s[i+3]=='e' or s[i+3]=='E':
                    if s[i+4]=='n' or s[i+4]=='N':
                        return 7
        return 0
    elif s[i]=='e' or s[i]=='E':
        if s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='g' or s[i+2]=='G':
                if s[i+3]=='h' or s[i+3]=='H':
                    if s[i+4]=='t' or s[i+4]=='T':
                        return 8
        return 0
    elif s[i]=='n' or s[i]=='N':
        if s[i+1]=='i' or s[i+1]=='I':
            if s[i+2]=='n' or s[i+2]=='N':
                if s[i+3]=='e' or s[i+3]=='E':
                    return 9
    
content=[]
for line in sys.stdin:
    content.append(line)

res =[]

for k in range(len(content)):
    a=0
    b=0
    first=True
    s=content[k]
    for i in range(len(s)):
        if isDigit(s, i) and first:
            a=getDigit(s, i)
            first=False
        elif isDigit(s, i) and not first:
            b=getDigit(s, i)
        
    if a!=0 and b!=0:
        res.append(10*a+b)
    else:
        res.append(10*a+a)

result = 0
for i in range(len(res)):
    result +=res[i]

print(result)



            