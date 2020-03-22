import Grid as G

# def userInput(userInput):
#     if userInput == 1:
#         return True
#     elif userInput == 0:
#         return False
#     else:
#         return None

myGrid = G.Grid()
# myGrid.setCell(0, 0, True)
# myGrid.setCell(1, 1, True)
# myGrid.setCell(2, 2, True)
# myGrid.printGrid()
# print(myGrid.checkWin())

w = None 
while w == None:
    myGrid.printGrid()
    # taking team True coordinates
    i = input("True team Row:\n")
    i = int(i)
    j = input("True team Col:\n")
    j = int(j)
    myGrid.setCell(i, j, True)
    myGrid.printGrid()
    # checking if True team wins
    if(myGrid.checkWin() == True):
        print("True team wins!\n")
        break
    # taking False team coordinates
    a = input("False team Row:\n")
    a = int(a)
    b = input("False team Col:\n")
    b = int(b)
    myGrid.setCell(a, b, False)
    # checking if False team wins
    if(myGrid.checkWin() == False):
        print("False team wins!\n")
        break
    # checking loop condition
    w = myGrid.checkWin()
   
   