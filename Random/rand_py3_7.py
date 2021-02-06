import random
import numpy as np
import time
import matplotlib.pyplot as plt
import math
import seaborn as sns
import pandas as pd


def rand_vs_np():
    rand_times = []
    np_times = []
    for n in range(100, 1000):
        start = time.clock()
        [random.random() for i in range(n)]
        rand_times.append(time.clock() - start)

    for n in range(100, 1000):
        start = time.clock()
        np.random.sample(n)
        np_times.append(time.clock() - start)

    y = [i for i in range(100, 1000)]
    plt.scatter(y, rand_times, color='teal', s=5)
    plt.scatter(y, np_times, color='blue', s=5)
    plt.xlabel('sample size')
    plt.ylabel('sort time')
    plt.savefig('rand_vs_np.png', format='png')
    plt.show()
    plt.close()


def text_shuffle():
    # Пусть непечатаемые символы тоже являются пунктуацией
    line = input('Enter some text: ')
    shuffled = ''
    inp_text = line.split()
    for word in inp_text:
        if len(word) > 2:
            new_w = word[0] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
            shuffled += new_w
        else:
            shuffled += word
        shuffled += ' '
    return shuffled


def random_walk():
    step_num = int(input('Enter number of steps: '))
    steps = np.random.choice(a=[0, -1, 1], size=(step_num, 2))
    path = np.concatenate([np.zeros((1, 2)), steps]).cumsum(0)
    plt.scatter(path[:, 0], path[:, 1], s=2, alpha=0.5, color='blue')
    plt.plot(0, 0, color='red', marker='o')
    plt.plot(path[-1:][:, 0], path[-1:][:, 1], color='red', marker='o')
    plt.plot(path[:, 0], path[:, 1], c='teal', alpha=0.5, lw=0.25, ls='-')
    plt.title('Random walk')
    plt.xlabel('x axis steps')
    plt.ylabel('y axis steps')
    plt.savefig('random_walk.png', format='png')
    plt.show()
    plt.close()


def sort_check(ch_list):
    for i in range(1, len(ch_list)):
        if ch_list[i - 1] > ch_list[i]:
            return 0
    return 1


def bogosort(data) -> list:
    while sort_check(data) != 1:
        random.shuffle(data)
    return data


def time_check(arr):
    start = time.clock()
    bogosort(arr)
    return time.clock() - start


def bogo_vis():
    final_list = []
    for j in range(4):
        times = []
        x = []
        for i in range(4, 11):
            samp = np.random.randint(0, 100, i)
            times.append(time_check(samp))
            x.append(i)
        final_list.append(times)
        print(*times)
    final_array = np.array(final_list)
    print(final_array)

    aver = np.average(final_array, axis=0)
    ln_aver = [math.log(av) for av in aver]
    disp = np.std([math.log(fin) for fin in final_array[j]], axis=0)
    x = np.array(x)

    plt.errorbar(x, ln_aver, yerr=disp)
    plt.plot(x, ln_aver)
    for j in range(4):
        plt.scatter(x, [math.log(fin) for fin in final_array[j]], color='red', s=5)
    plt.ylabel('time ln(seconds)')
    plt.xlabel('array size')
    plt.title('Bogosort time')
    plt.savefig('bogosort_time.png', format='png')
    plt.show()
    plt.close()


random_walk()
#rand_vs_np()
#print(text_shuffle())
#bogo_vis()
