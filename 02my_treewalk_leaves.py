# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #13
#   modified original function computeHeight
#   looking at leaves only
# results
#   Failed case #22/24: time limit exceeded
#   Time used: 6.07/3.00, memory used: 37928960/536870912.
#
# summary: using np.where for ternary logic
#   start with leaves, size of array = n of leaves
#   find leaves parents (recursively), find unique, remove -1
#   count # of levels.
#   best performance so far, but short of required 3 seconds for case #22, 23
#
# last change: not using a fixed size array; dynamically reducing it while looping


import sys, threading
import time #to track time
import numpy as np

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:

    def read(self):
        # given:
        #self.n = int(sys.stdin.readline())
        #self.parent = np.array(sys.stdin.readline().split(),int)

        # hardcoded examples
        # ex1
        #self.n = 5  # int(sys.stdin.readline())
        #temp = '-1 0 4 0 3' #'4 -1 4 1 1'  #
        # ex2
        self.n = 10
        temp = '8 8 5 6 7 3 1 6 -1 5'
        self.parent = np.array(temp.split(), int)

        self.idx = np.arange(self.n)
        # get root
        self.root = np.where(self.parent==-1)[0][0]
        # find leaves
        self.leaves = np.setdiff1d(self.idx, self.parent)


    # my recursive function - only look at leaves
    def compute_height(self):
        height = 1

        while not (self.leaves.size == 1 and self.leaves[0]==self.root):
            print (self.leaves)
            height += 1
            _leaves = np.unique(self.parent[self.leaves])
            self.leaves = _leaves[_leaves != -1]
            _leaves = None

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