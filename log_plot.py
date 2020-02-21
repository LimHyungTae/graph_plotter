#!/usr/bin/env python


# author: mason


from math import atan2, pow, sqrt, sin, cos, tan

# import time

import numpy as np

import matplotlib.pyplot as plt

import sys

import signal


def signal_handler(signal, frame):  # ctrl + c -> exit program
    print('You pressed Ctrl+C!')
    sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':

    # as many options as possible to be used and searchable easily.


    ''' For Graph '''

    plt.figure(figsize=(10, 12))
    plt.title('Test')
    plt.xlabel('X data')
    plt.ylabel('Y data-log')
    plt.grid(color='gray', linestyle='dotted', alpha=0.8)
    plt.xlim(1, 100)
    plt.ylim(1, 10000000)

    ''' log scale!! '''

    plt.yscale("log")  ########

    line, = plt.plot([], [], color='blue', label='data', linewidth=0.7, alpha=0.8)
    line2, = plt.plot([], [], color='red', label='data2', linewidth=0.7, alpha=0.8)
    plt.legend(loc='upper left')
    x = np.linspace(1, 100, num=100)
    y = x ** 2
    y2 = abs(x ** 3 * np.sin(x))
    line.set_data(x, y)
    line2.set_data(x, y2)
    plt.tight_layout()
    plt.show()
    fig = plt.gcf()
    plt.show()
    fig.savefig("log.png")


