import random
sandl={24:5,38:12,47:23,70:36,80:55,98:58,57:27,34:19,45:14,76:18}
def movedice(playerpos,dice):
    newpos=playerpos+dice
    print("before position is",newpos)
    if newpos in sandl:
        newpos=sandl[newpos]
        print("you are bitten by a snake")
        return newpos
    elif newpos in sandl.values():
        for i in sandl:
            if sandl[i]==newpos:
                newpos=i
                break
        print("congo!you found a ladder")
        return newpos
    else:
        return newpos
def printboard(playerpos):
    pos=21
    for row in range(10,0,-1):
        for col in range(1,11):
            newno=(row)*10-col
            if newno==playerpos:
                print("[p]",end=" ")
            elif newno in sandl:
                print("[s]",end=" ")
            else:
                print("[-]",end=" ")
        print()
def diceroll():
    return random.randint(1,6)
print("welcome to snake and ladder game")
print("-"*50)
playerpos=0
while playerpos<100:
    print("player position is at",playerpos)
    input("press enter to start")
    dice=diceroll()
    print("your lucky no is",dice)
    move=movedice(playerpos,dice)
    print("your new position is",move)
    playerpos=move
    print()
    printboard(playerpos)
    print()
    print("+"*50)
print("hip hip hurray")