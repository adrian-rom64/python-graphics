import numpy as np
from enum import Enum
import png
import math


class ArrayType(Enum):
    black_white = 0
    greyscale = 1
    color = 2


def new_array(y, x, mode=ArrayType.black_white):
    if mode == ArrayType.greyscale:
        return np.zeros((x, y), dtype=float)
    elif mode == ArrayType.color:
        return np.zeros((x, y, 3), dtype=int)
    else:
        return np.zeros((x, y), dtype=int)


arr = new_array(3, 5, mode=ArrayType.greyscale)
for y in range(3):
    arr[y][0] = 0.7


def save_black_white(arr):
    arr[arr == 1] = 255
    png.from_array(arr.astype('uint8'), 'L').save('result.png')


def save_greyscale(arr):
    for i in range(np.shape(arr)[0]):
        for j in range(np.shape(arr)[1]):
            if (arr[i][j] == 1):
                arr[i][j] = 255
            else:
                arr[i][j] = arr[i][j] * 256
    png.from_array(arr.astype('uint8'), 'L').save('result.png')


save_greyscale(arr)
