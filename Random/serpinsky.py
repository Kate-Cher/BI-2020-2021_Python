import numpy as np
import matplotlib.pyplot as plt

axp = []
for i in range(3):
    axp.append(np.random.randint(0, 100, 2))
start = np.random.randint(0, 100, 2)
n = 50000
points = [tuple(start)]

path = np.random.choice(a=[0, 1, 2], size=n)
for i in range(len(path)):
    p = axp[path[i]]
    points.append(tuple([((p[0] + points[i][0]) / 2), ((p[1] + points[i][1]) / 2)]))
points = np.array(points)

plt.scatter(points[:, 0], points[:, 1], s=0.5, alpha=0.5)
for i in range(3):
    plt.scatter(axp[i][0], axp[i][1], color='red', s=20)
plt.scatter(start[0], start[1], color='black', s=20)
plt.savefig('serpinsky_fin.png', format='png')
plt.show()
plt.close()