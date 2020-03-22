import Cell as C

class Grid:
    """
    Grid schema:
    00 01 02
    10 11 12
    20 21 22
    """
    grid = [] # initializing an empty grid
    def __init__(self):
        for i in range(3):
            row = []
            for j in range(3):
                cell = C.Cell()
                row.insert(j, cell)
            self.grid.insert(i, row)
    
    def setCell(self, row, col, team):
        if self.grid[row][col].getState() == None:  
            self.grid[row][col].setState(team)
        else:
            print("Error: cell already occupied.\n")

    def checkWin(self):
        # checking diagonals
        if self.grid[0][0].getState() != None and self.grid[0][0].getState() == self.grid[1][1].getState() and self.grid[0][0].getState() == self.grid[2][2].getState():
            return self.grid[0][0].getState()
        if self.grid[0][2].getState() != None and self.grid[0][2].getState() == self.grid[1][1].getState() and self.grid[0][2].getState() == self.grid[2][0].getState():
            return self.grid[0][2].getState()
        # checking rows and columns
        for i in range(3):
            if(self.grid[i][0].getState() != None and self.grid[i][0].getState() == self.grid[i][1].getState() and self.grid[i][1].getState() == self.grid[i][2].getState()):
                return self.grid[i][0].getState()
        for j in range(3):
            if(self.grid[0][j].getState() != None and self.grid[0][j].getState() == self.grid[1][j].getState() and self.grid[1][j].getState() == self.grid[2][j].getState()):
                return self.grid[0][j].getState()
        return None # no one wins, still

    def printGrid(self):
        for i in range(len(self.grid)):
            print("{}\t{}\t{}\n".format(self.grid[i][0].getState(), self.grid[i][1].getState(), self.grid[i][2].getState()))
    
        
