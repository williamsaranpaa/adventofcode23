import sys
import re


content=[]
for line in sys.stdin:
    content.append(line)

games = []
for i in range(len(content)):
    temp = content[i].split(':')[1].split(';')
    game=[]
    for j in range(len(temp)):
        red =re.findall('[0-9]+ red',temp[j])
        green =re.findall('[0-9]+ green',temp[j])
        blue =re.findall('[0-9]+ blue',temp[j])
        if len(red)!=0:
            r=re.findall('[0-9]+', red[0])
        else:
            r='0'
        if len(green)!=0:
            g=re.findall('[0-9]+', green[0])
        else:
            g='0'
        if len(blue)!=0:
            b=re.findall('[0-9]+', blue[0])
        else:
            b='0'
        
        game.append([int(r[0]),int(g[0]),int(b[0])])
    games.append(game)

res=0
for i in range(len(games)):
    r=0
    g=0
    b=0
    for j in range(len(games[i])):
        if games[i][j][0]>r:
            r=games[i][j][0]
        if games[i][j][1]>g:
            g=games[i][j][1]
        if games[i][j][2]>b:
            b=games[i][j][2]
    res+=r*g*b

print(res)