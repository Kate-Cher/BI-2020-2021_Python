import matplotlib.pyplot as plt
import numpy as np
# Random numbers distribution
xs = sorted(np.random.randint(-100, 100, 20))
ys = sorted(np.random.randint(-30, 30, 20))
plt.plot(xs, ys, color = 'teal', marker = 'o')
plt.title('Random numbers distribution')
plt.xlabel('Abscissa value')
plt.ylabel('Ordinate value')
plt.savefig('Random_nums.png')
plt.show()
plt.savefig("Random_num.png")