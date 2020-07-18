import random
from cell import Cell

def get_dirt():
    num = random.randint(2, 6)
    dirt = list()

    for i in range(num):
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        temp = Cell(x, y)
        if temp not in dirt:
            dirt.append(temp)

    dirt.sort()

    return dirt

def find_path(dirt_list):
    pos = Cell(0, 0)
    path = list()
    path.append(pos)

    for dirt in dirt_list:
        flag = True
        
        while flag:
            pos = path[-1]
            if dirt.x < pos.x:
                x = pos.x - 1
                y = pos.y
                temp = Cell(x, y)
                path.append(temp)
            elif dirt.x > pos.x:
                x = pos.x + 1
                y = pos.y
                temp = Cell(x, y)
                path.append(temp)
            elif dirt.x == pos.x:
                if dirt.y < pos.y:
                    x = pos.x
                    y = pos.y - 1
                    temp = Cell(x, y)
                    path.append(temp)
                elif dirt.y > pos.y:
                    x = pos.x
                    y = pos.y + 1
                    temp = Cell(x, y)
                    path.append(temp)
                elif dirt.y == dirt.y:
                    flag = False
    
    return path    

def is_present(cell, temp):
    return (cell.x == temp.x and cell.y == temp.y)
