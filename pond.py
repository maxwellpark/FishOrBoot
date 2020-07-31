from random import randint 

# pond surface is visible to players (shows which gridcells have been prospected)
def renderPondSurface(rows, cols, pondSurface):
    print("____" * cols)     
    for i in range(rows):
        for j in range(cols):
            # True signifies that it's already been attempted
            if (pondSurface[i][j] == False):
                if (j < 1):
                    print("|", end="") 
                print("___|", end="")
            else:
                if (j < 1):
                    print("|_X_|", end="")
                else:
                    print("_X_|", end="")
        print("") 

def checkForFish(x, y, pondLife):
    return False if (pondLife[x][y] == 0) else True 

def castLine(x, y, player, pondLife, pondSurface):
    if (checkForFish(x, y, pondLife)):
        pondSurface[x][y] = True 
        player.fishCaught += 1
    else: 
        pondSurface[x][y] = True 
        player.bootsCaught += 1
