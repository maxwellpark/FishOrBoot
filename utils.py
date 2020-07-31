import config 

# input validation for xy coordinates
def validateCoordinate(player, axis, maximum): 
    while 1: 
        if axis == "x":
            try:
                x = int(input(f"{player.name}, Enter x coordinate: "))
                if x >= 0 and x <= maximum:
                    return x 
            except (TypeError, ValueError) as e:
                print(f"x coordinate must be an integer between 0 and {maximum}")
        elif axis == "y":
            try:
                y = int(input(f"{player.name}, Enter y coordinate: "))
                if y >= 0 and y <= maximum:
                    return y 
            except (TypeError, ValueError) as e:
                print(f"y coordinate must be an integer between 0 and {maximum}")

# input validation for grid dimensions
def validateDimension(axis):
    while 1:
        if axis == "x":
            try:
                cols = int(input("Enter no. of columns: "))
                if cols > 0 and cols < config.MAX_POND_SIZE: 
                    return cols 
            except (TypeError, ValueError) as e:
                print(f"Columns value must be an integer between 1 and {config.MAX_POND_SIZE}")

        if axis == "y":
            try:
                rows = int(input("Enter no. of rows: "))
                if rows > 0 and rows < config.MAX_POND_SIZE: 
                    return rows 
            except (TypeError, ValueError) as e:
                print(f"Rows value must be an integer between 1 and {config.MAX_POND_SIZE}")