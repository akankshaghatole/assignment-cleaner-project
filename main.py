from environment import Environment
from functions import get_dirt, find_path, is_present

def main():
    dirt = get_dirt()
    path = find_path(dirt)  
    env = Environment(dirt)

    for pos in path:
        if is_present(pos, dirt[0]):
            dirt.remove(dirt[0])
            env.update(pos.x, pos.y, flag= True)
        else:
            env.update(pos.x, pos.y)

main()
