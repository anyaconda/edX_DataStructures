# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
#   only looking at leaf nodes - reduce unnecessary trips to non-leaves
#   lists and diff between 2 lists


import sys, threading
import time #to track time
import numpy as np

sys.setrecursionlimit(10**4) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

        #hardcoded examples
        #self.n = 5  # int(sys.stdin.readline())
        #self.parent = [4, -1, 4, 1, 1]  # [-1, 0, 4, 0, 3] #list(map(int, sys.stdin.readline().split()))

        #self.n = 100
        #self.parent = list(map(int, '91 54 74 11 89 96 81 32 83 28 66 72 51 24 58 19 97 88 34 37 77 10 61 99 64 47 -1 92 45 39 69 52 42 63 13 85 18 25 57 76 56 16 21 14 12 50 59 7 5 30 84 87 40 22 98 71 46 65 93 53 49 4 48 78 82 31 55 70 3 33 17 67 20 86 6 60 94 26 38 29 44 23 27 41 36 80 8 73 79 2 1 75 15 95 43 68 35 90 9 62'.split()))

        self.me = list(range(self.n))
        # find leaves
        self.leaves = list(set(self.me) - set(self.parent))


    # my recursive function - only look at leaves
    def compute_height(self):

        maxHeight = 0
        for vertex in self.leaves:
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;

    #original recursive function
    def compute_height0(self):
        # Replace this code with a faster implementation
        maxHeight = 0

        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height);
        return maxHeight;


def main():
    # track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()
    # original call to compute tree height
    print(myTree.compute_height())

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()
