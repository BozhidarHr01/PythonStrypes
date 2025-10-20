from data import *

def maze_recursive(maze, x, y, is_path = False):
    cls()

    if maze[x][y] == '🏁':
        maze[x][y] = '✅'
        print_matrix(maze)
        print("exit found")
        is_path = True
        return

    if is_path:
        return

    if maze[x][y] == '🧱':
        return

    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return

    if maze[x][y] != '❌':
        maze[x][y] = '❌'
    else:
        return

    print_matrix(maze)
    print('\n')
    input("enter for next move")

    maze_recursive(maze, x + 1, y, is_path)
    maze_recursive(maze, x, y + 1, is_path)
    maze_recursive(maze, x, y - 1, is_path)
    maze_recursive(maze, x - 1, y, is_path)

maze_recursive(grid, 1, 1)
