from data import *

def maze_iterative(maze, start_x, start_y):
    stack = [(start_x, start_y, [])]

    while stack:
        x, y, path = stack.pop()
        cls()

        if maze[x][y] == '🏁':
            maze[x][y] = '✅'
            for px, py in path:
                maze[px][py] = '🟢'
            maze[start_x][start_y] = '🟢' 
            print("exit found")
            print_matrix(maze)
            return True

        if maze[x][y] == '🧱':
            continue

        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
            continue

        if maze[x][y] != '❌':
            maze[x][y] = '❌'
        else:
            continue

        print_matrix(maze)
        print('\n')
        input("enter for next move")

        new_path = path + [(x, y)]

        stack.append((x - 1, y, new_path))
        stack.append((x, y - 1, new_path))
        stack.append((x, y + 1, new_path))
        stack.append((x + 1, y, new_path))

    print("no exit found")
    return False
    
maze_iterative(grid, 1, 1)