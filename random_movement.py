import sys
import math
from random import *


width, height, my_id = [int(i) for i in input().split()]
xyPath = []
surface = 0
islands=""

def island_find():
    global islands
    for i in range(height):
        line = input()
        # print(i,file=sys.stderr)
        # print(line,file=sys.stderr)
        index = 0
        for ch in line:
            if ch == "x":
                islands = islands + " //" + " " + str(index) + " " + str(i)
            index = index+1

    print("islands =", file=sys.stderr)
    print(islands, file=sys.stderr)

def spawn():
    #Random spawn
    while True:
        startX = str(randint(0, 14))
        startY = str(randint(0, 14))
        startpos = " "+startX + " " + startY + " "
        if startpos in islands:
            continue
            #print("spawn sur ile => RETRY", file=sys.stderr)
        else:
            break

    print("SPAWN :", file=sys.stderr)
    print(startpos, file=sys.stderr)
    xyPath.append(startX + " " + startY)
    firstX, firstY = str(xyPath[0]).split(" ")
    print(firstX+" "+firstY)

def pathfinding(x, y):
    global surface

    banlist = ""
    while True:
        int = randint(1, 4)
        if int == 1:
            dir = "S"
            nextX = x
            nextY = y+1
        if int == 2:
            dir = "W"
            nextX = x-1
            nextY = y
        if int == 3:
            dir = "N"
            nextX = x
            nextY = y-1
        if int == 4:
            dir = "E"
            nextX = x+1
            nextY = y

        if ("E" in banlist) and ("W" in banlist) and ("N" in banlist) and ("S"in banlist):
            print("---------jsuis bloké---------", file=sys.stderr)
            surface = 1
            break

        print("------ON TENTE : "+dir+"-----------", file=sys.stderr)
        print("banlist = "+banlist, file=sys.stderr)
        print("current pos X = " + str(x) + "Y = " + str(y), file=sys.stderr)
        print("next=", file=sys.stderr)
        flag = 0
        next = str(nextX)+" "+str(nextY)
        print(next, file=sys.stderr)

        if (dir in banlist):
            print("deja tenté => RETRY", file=sys.stderr)
            if dir not in banlist:
                banlist = banlist + dir
            flag = 0
            continue
        if ((" "+next+" ") in islands):
            print("touche une ile => RETRY", file=sys.stderr)
            if dir not in banlist:
                banlist = banlist + dir
            flag = 0
            continue
        if ("15" in next) or ("-1" in next):
            print("touche une bordure => RETRY", file=sys.stderr)
            if dir not in banlist:
                banlist = banlist + dir
            flag = 0
            continue
        print("lengthxypath = "+str(len(xyPath)), file=sys.stderr)
        for i in range(len(xyPath)):
            if (str(xyPath[i]) == next):
                print(str(xyPath[i]), file=sys.stderr)
                print("revient sur ses pas => RETRY", file=sys.stderr)
                if dir not in banlist:
                    banlist = banlist + dir
                flag = 0
                break
            else:
                print("c bon, dir = "+dir, file=sys.stderr)
                flag = flag+1
        print("flag = " + str(flag), file=sys.stderr)

        if flag > 0:
            break

        else:
            continue
    xyPath.append(str(nextX)+" "+str(nextY))
    print("blok="+str(surface), file=sys.stderr)
    return dir


# game loop

island_find()
spawn()

while True:
    x, y, my_life, opp_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown = [
        int(i) for i in input().split()]
    
    sonar_result = input()
    opponent_orders = input()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    dir = pathfinding(x, y)

    print("sorti de boucle", file=sys.stderr)
    print("surface="+str(surface), file=sys.stderr)
    
    if surface == 1:
        action = "SURFACE"
        surface = 0
    else:
        action = "MOVE " + dir + " " + "TORPEDO"

    if "SURFACE" in action:
        xyPath.clear()
        xyPath.append(str(x) + " " + str(y))

    print(action)
