# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #12
#   modified original function computeHeight
#   looking at leaves only
# results
#   Failed case #22/24: time limit exceeded
#   Time used: 6.51/3.00, memory used: 56582144/536870912
#
# summary: using np.where for ternary logic
#   start with leaves, size of array = n of leaves
#   find leaves parents (recursively), when done set to -1
#   count # of levels.
#   best performance so far, but short of required 3 seconds for case #22, 23
#
# last change: not using flag 'done'


import sys, threading
import time #to track time
import numpy as np

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:

    def read(self):
        # given:
        self.n = int(sys.stdin.readline())
        self.parent = np.array(sys.stdin.readline().split(),int)

        # hardcoded examples
        # ex1
        #self.n = 5  # int(sys.stdin.readline())
        #temp = '4 -1 4 1 1'  # [-1, 0, 4, 0, 3] #
        # ex2
        #self.n = 10
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = np.array(temp.split(), int)

        self.idx = np.arange(self.n)
        # find leaves
        self.leaves = np.setdiff1d(self.idx, self.parent)


    # my recursive function - only look at leaves
    def compute_height(self):
        height = 0

        while not np.all(self.leaves == -1):
            #print (self.leaves)
            height += 1
            self.leaves = np.where(self.leaves > -1, self.parent[self.leaves], -1)

        return height


    # # my recursive function1 - only look at leaves
    # def compute_height1(self):
    #     maxHeight = 0
    #
    #     for vertex in self.leaves:
    #         height = 0
    #         i = vertex
    #         while i != -1:
    #             height += 1
    #             i = self.parent[i]
    #         maxHeight = max(maxHeight, height);
    #     return maxHeight;
    #
    # #original recursive function
    # def compute_height0(self):
    #     # Replace this code with a faster implementation
    #     maxHeight = 0
    #
    #     for vertex in range(self.n):
    #         height = 0
    #         i = vertex
    #         while i != -1:
    #             height += 1
    #             i = self.parent[i]
    #         maxHeight = max(maxHeight, height);
    #     return maxHeight;


def main():
    # track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()
    # compute tree height
    print (myTree.compute_height())

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()