import time
from cell import Cell

class Environment:
    vacc = Cell(0, 0)
    
    def __init__(self, dirt): 
        self.env = [['-' for i in range(10)] for j in range(10)]
        self.env[self.vacc.y][self.vacc.x] = 'C'

        for cell in dirt:
            self.env[cell.y][cell.x] = 'D' 

        for lis in self.env:
            print(lis)
    
    def update(self, x, y, flag= False):
        # self.env[self.vacc.y][self.vacc.x] = '-'
        self.vacc = Cell(x, y)
        self.env[self.vacc.y][self.vacc.x] = 'C'

        print()
        print()
        if flag:
            print("Cleaned dirt at position: ({}, {})".format(x, y))
        time.sleep(1)
        for lis in self.env:
            print(lis)
