import random , time, copy
from tkinter.tix import Tree
from turtle import right
WIDTH = 6
HEIGHT = 6
nextCell =[]
for x in range(WIDTH):
    column=[]
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') #Add a living cell
        else:
            column.append(" ")# Add a dead cell
    nextCell.append(column)

while True:
    print('\n\n\n\n\n')
    currentCell = copy.deepcopy(nextCell)

    # This print the currentCell on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCell[x][y],end=" ")
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x-1)%WIDTH
            rightCoord = (x+1)%WIDTH
            aboveCoord = (y-1)%HEIGHT
            belowCoord = (y+1)%HEIGHT

            numNeighbour =0
            if currentCell[leftCoord][aboveCoord]=='#':
                numNeighbour+=1
            if currentCell[x][aboveCoord] =='#':
                numNeighbour+=1
            if currentCell[rightCoord][aboveCoord]=='#':
                numNeighbour+=1
            if currentCell[leftCoord][y]=='#':
                numNeighbour+=1
            if currentCell[rightCoord][y]=='#':
                numNeighbour+=1
            if currentCell[leftCoord][belowCoord]=='#':
                numNeighbour+=1
            if currentCell[x][belowCoord]=='#':
                numNeighbour+=1
            if currentCell[rightCoord][belowCoord]=='#':
                numNeighbour+=1

            if currentCell[x][y] =='#' and (numNeighbour ==2 or numNeighbour==3):
                nextCell[x][y]='#'

            elif currentCell[x][y]==' ' and (numNeighbour ==2 or numNeighbour==3):
                nextCell[x][y]='#'
            else:
                nextCell[x][y]=' '
    time.sleep(1) #Add a 1-second pause to reduce flickering
    
