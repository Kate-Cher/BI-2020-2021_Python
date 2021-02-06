import numpy as np
import matplotlib.pyplot as plt

apx = [[0, 0], [1, 0], [0, 1], [1, 1], [0, 0.5], [0.5, 0], [0.5, 1], [1, 0.5]]

n = 50000
points = [tuple(np.random.randint(0, 2, 2))]

path = np.random.choice(a=[i for i in range(8)], size=n)

for i in range(len(path)):
    p = apx[path[i]]
    points.append(tuple([((2 * p[0] + points[i][0]) / 3), ((2 * p[1] + points[i][1]) / 3)]))
points = np.array(points)

plt.scatter(points[:, 0], points[:, 1], s=0.5, alpha=0.5)
plt.savefig('serpinsky_carp.png', format='png')
plt.show()
plt.close()
