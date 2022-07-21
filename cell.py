import pygame

class cell:
    aroundMines = 0
    image = "Images/standart.png"

    def __init__(self, number, x, y, mine, flag):
        self.number = number
        self.x = x
        self.y = y
        self.mine = mine
        self.flag = flag

    def clickOnIt(self, x, y):
        pass

    def countMines(self, cellsList):
        self.aroundMines = 0
        for i in cellsList:
            if i.x == self.x and i.y == self.y:
                continue
            elif i.x == self.x-1 and i.y == self.y+1 and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x and i.y == self.y+1 and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x+1 and i.y == self.y+1 and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x-1 and i.y == self.y and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x+1 and i.y == self.y and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x-1 and i.y == self.y-1 and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x and i.y == self.y-1 and i.mine == True:
                self.aroundMines += 1
            elif i.x == self.x+1 and i.y == self.y-1 and i.mine == True:
                self.aroundMines += 1

    def toString(self):
        print(self.number, self.x, self.y, self.mine, self.flag)