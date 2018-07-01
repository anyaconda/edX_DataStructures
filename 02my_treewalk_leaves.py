# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# After submission 8, failed case #16 time limit exceeded
#   computeHeight - returned to going through leaves, previous success with speed
#
#   only looking at leaf nodes - reduce unnecessary trips to non-leaves
#   lists and diff between 2 lists
#   strategy: start with leaves, recursively look at parents until end up with the root node (or more)
#   main datastruct array, no more lists or sets
#
# after submission #9 - slight improvements shaving off seconds
#   modified original function computeHeight
#   array instead of list, recursive compute; looking at leaf nodes only
# results
#   Failed case #22/24: time limit exceeded
#   Time used: 6.12/3.00, memory used: 1149603840/536870912.
#
# last change: using np.where for ternary logic
#   start with leaves, size of array = n of leaves
#   find leaves parents (recursively), if encounter -1 set back to root node value
#   do until last level all equal root
#   count # of levels.
#   best performance so far, but short of required 3 seconds for case #22, 23
#
#  next: build a matrix and just count number of rows in matrix


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
        #get root
        self.root = np.where(self.parent==-1)[0][0]
        # find leaves
        self.leaves = np.setdiff1d(self.idx, self.parent)
        self.parents = np.arange(self.leaves.size)

    # my recursive function - only look at leaves
    height = 0
    done = 0

    def compute_height(self, nodes):

        while not self.done:
            self.height += 1
            self.parents = np.where(nodes > -1, self.parent[nodes], -1)

            #look for nodes that found root
            if not np.argwhere(self.parents == -1).size==self.leaves.size:

            #check if this level still has nodes to process
            #if not done_idx.size==self.leaves.size:
                self.compute_height(self.parents)
            else:
                self.done=1


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
    myTree.compute_height(myTree.leaves)
    print(myTree.height)

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()
