import numpy as np
import matplotlib.pyplot as plt

maze = np.array([[0, 0, 0, 0, 0, 0, 0],
                 [3, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 3],
                 [0, 0, 0, 0, 0, 0, 0]])
plt.subplot(121)
plt.imshow(maze)


def solve(maze, pos, exitPos):
    maze[pos] = 3
    if pos == exitPos:
        plt.subplot(122)
        plt.imshow(maze)
        return True

    r, c = pos

    neighbours = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
    for posi in neighbours:
        if maze[posi] == 1:
            if solve(maze, posi, exitPos):
                return True

    maze[pos] = 2

    return False


solve(maze.copy(), (1, 1), (3, 5))
plt.show()
