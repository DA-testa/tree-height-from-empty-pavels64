#python 3

import sys
import threading
import numpy

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

def compute_height(n, parents):
    nodes = [Node(i) for i in range(n)]
    root = None
    
    for i, parent_index in enumerate(parents):
        if parent_index == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent_index]
            parent_node.add_child(nodes[i])
    
    max_depth = 0
    
    def dfs(node, depth):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        for child in node.children:
            dfs(child, depth+1)
    
    dfs(root, 1)
    
    return max_depth

def main():
    try:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()

