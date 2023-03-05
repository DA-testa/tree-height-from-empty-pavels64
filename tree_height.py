#python 3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    heights = np.zeros(int(n))
    max_height = 0
    for i in range(int(n)):
        if heights[i] > 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heights[j] > 0:
                height += heights[j]
                break
            else:
                height += 1
                j = int(parents[j])
        heights[i] = height
        if height > max_height:
            max_height = height
    return max_height

def input_from_keyboard():
    n = input().strip()
    if n is not None:
        parents = input().strip().split(" ")
        if parents:
            return n, parents
    return None, None

def input_from_file(file_dir):
    try:
        with open(f"./test/{file_dir}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("ERROR: File not found.")
        return None, None

    n = contents[0].strip()
    if n is not None:
        parents = contents[1].strip().split(" ")
        if parents:
            f.close()
            return n, parents
    return None, None

def main():
    input_method = input().strip()
    if input_method == "F":
        file_dir = input().strip()
        if str(file_dir[-1]) != "a":
            n, parents = input_from_file(file_dir)
            if n is not None and parents is not None:
                height = compute_height(n, parents)
                print(int(height))
    elif input_method == "I":
        n, parents = input_from_keyboard()
        if n is not None and parents is not None:
            height = compute_height(n, parents)
            print(int(height))

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()


