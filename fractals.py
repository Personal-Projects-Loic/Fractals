#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def settings():
    width, height = 8000, 8000
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    max_iter = 300
    c = complex(-0.8, 0.156)
    return width, height, x_min, x_max, y_min, y_max, max_iter, c

def complexGrid(x_min, x_max, y_min, y_max, width, height):
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    return X + 1j * Y

def formula(Z, max_iter, c):
    escape_time = np.zeros(Z.shape, dtype=int)
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + c
        escape_time[mask] += 1
    return escape_time

def displaymMtplotlib(escape_time, x_min, x_max, y_min, y_max, c):
    plt.figure(figsize=(10, 10))
    plt.imshow(escape_time, extent=(x_min, x_max, y_min, y_max), cmap="hot")
    plt.colorbar(label="Nombre d'itérations")
    plt.title(f"Fractale de Julia pour c = {c}")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()

def main():
    width, height, x_min, x_max, y_min, y_max, max_iter, c = settings()
    Z = complexGrid(x_min, x_max, y_min, y_max, width, height)
    escape_time = formula(Z, max_iter, c)
    displaymMtplotlib(escape_time, x_min, x_max, y_min, y_max, c)

if __name__ == "__main__":
    main()
