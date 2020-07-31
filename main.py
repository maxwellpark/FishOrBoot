import fisherman
from pond import renderPondSurface, checkForFish, castLine
from utils import validateCoordinate, validateDimension 
from random import randint 

# array of ints to represent fish and boots in each cell of the pond grid
pondLife = [] 

# array of bools to represent which cells have already been visited 
# this data is displayed to the player each turn (hides the fish and boots underneath) 
pondSurface = []

# pond grid dimensions 
rows = 0
cols = 0 

def gameLoop():
    gameOver = False
 
    # initialise player objects
    Player1 = fisherman.Fisherman(input("Player 1, Enter Your Name: "))    
    Player2 = fisherman.Fisherman(input("Player 2, Enter Your Name: "))

    # create the pond environment with custom dimensions (user input) and random fish/boot values
    rows = validateDimension("y")
    print(rows)
    cols = validateDimension("x")
    print(cols)

    pondLife = [[randint(0, 1) for j in range(cols)] for i in range(rows)] 
    pondSurface = [[False] * cols for i in range(rows)]

    renderPondSurface(rows, cols, pondSurface) 
    
    while not gameOver:
        # player 1's turn  
        x = validateCoordinate(Player1, "x", cols - 1)
        y = validateCoordinate(Player1, "y", rows - 1)
        
        castLine(x, y, Player1, pondLife, pondSurface)
        renderPondSurface(rows, cols, pondSurface)
        print(f"{Player1.name} has caught {Player1.fishCaught} fish.")                                               
        print(f"{Player1.name} has caught {Player1.bootsCaught} boot(s).")
        # handleMove(Player1)
        
        # player 2's turn
        x = validateCoordinate(Player2, "x", cols - 1)
        y = validateCoordinate(Player2, "y", rows - 1)
        castLine(x, y, Player2, pondLife, pondSurface)
        renderPondSurface(rows, cols, pondSurface)
        print(f"{Player2.name} has caught {Player2.fishCaught} fish.")                                           
        print(f"{Player2.name} has caught {Player2.bootsCaught} boot(s).")

        # check if game is over (all pond cells visited)
        if (not any(False in row for row in pondSurface)):
            gameOver = True 
            if (Player1.fishCaught == Player2.fishCaught):
                print(f"It's a draw! With {Player1.fishCaught} fish a piece!") 
            else:
                winner = Player1 if (Player1.fishCaught > Player2.fishCaught) else Player2
                print(f"{winner.name} wins with {winner.fishCaught} fish!")

            restartGame = input("Press Enter to play again.") 
            if (restartGame == ""):
                gameLoop()

# this is primarily here to prevent duplicate moves
# but it also abstracts away implementation details 
def handleMove(player):
    while 1:
        x = validateCoordinate(player, "x", cols - 1)
        y = validateCoordinate(player, "y", rows - 1)
        if pondSurface[x][y]:
            print("This cell has already been prospected. Try a different cell.")
        else:
            break 
    castLine(x, y, Player1, pondLife, pondSurface)
    renderPondSurface(rows, cols, pondSurface)
    print(f"{Player1.name} has caught {Player1.fishCaught} fish.")                                               
    print(f"{Player1.name} has caught {Player1.bootsCaught} boot(s).")

# entry point  
gameLoop()