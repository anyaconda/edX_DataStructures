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
# submission #9 - much progress.  progressed to case #22
#   modified original function computeHeight
#   array instead of list, recursive compute; looking at leaf nodes only
# results
#   Failed case #22/24: time limit exceeded
#   Time used: 6.12/3.00, memory used: 1149603840/536870912.


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
    height = 0
    done = 0

    def compute_height(self, nodes):

        while not self.done:
            parents = self.parent[nodes]
            parents_clean = np.unique(parents)
            self.height += 1
            #print (parents_clean)
            #print(parents_clean.size)

            if np.where(parents_clean==-1)[0]==0 and parents_clean.size==1:
                self.done = 1
            else:
                parents_clean = parents_clean[parents_clean != -1]

                self.compute_height(parents_clean)


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
    # original call to compute tree height
    myTree.compute_height(myTree.leaves)
    print(myTree.height)

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()
