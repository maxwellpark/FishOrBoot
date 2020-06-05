import fisherman
from pond import renderPondSurface, checkForFish, castLine
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

    # create the pond environment with custom dimensions and random values
    rows = int(input("Enter no. of rows: "))
    cols = int(input("Enter no. of columns: "))
    pondLife = [[randint(0, 1) for j in range(cols)] for i in range(rows)] 
    pondSurface = [[False] * cols for i in range(rows)]
    print(pondSurface) 

    renderPondSurface(rows, cols, pondSurface) 
    
    while not gameOver:
        # player 1's turn  
        x = int(input(f"{Player1.name}, Enter x coordinate: "))
        y = int(input(f"{Player1.name}, Enter y coordinate: ")) 
        castLine(x, y, Player1, pondLife, pondSurface)
        renderPondSurface(rows, cols, pondSurface)
        print(f"{Player1.name} has caught {Player1.fishCaught} fish.")                                               
        print(f"{Player1.name} has caught {Player1.bootsCaught} boot(s).")
        
        # player 2's turn
        x = int(input(f"{Player2.name}, Enter x coordinate: "))
        y = int(input(f"{Player2.name}, Enter y coordinate: "))
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

gameLoop()
