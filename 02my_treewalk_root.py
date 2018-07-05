# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# For submission 10,
#   computeHeight - starting from root and looking at kids at each level
#       (instead of going through leaves)
#
#   main datastruct numpy array - looking up kids by sending np.array of parents
#   relying on np.in1d
#
# results
#   Failed case #18/24: time limit exceeded (locally 14 seconds)
#   Time used: 6.10/3.00, memory used: 37318656/536870912.


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

        #get root
        self.root = np.where(self.parent==-1)[0]

        # self.idx = np.arange(self.n)
        # find leaves
        #self.leaves = np.setdiff1d(self.idx, self.parent)
        #self.parents = np.arange(self.leaves.size)

    # my recursive function - start from root, look for kids until no kids
    height = 0
    done = 0

    def compute_height(self, nodes):

        while not self.done:
            #print (nodes)
            self.height += 1
            # find kids
            kids = np.nonzero(np.in1d(self.parent, nodes))[0]
            #print('kids ', kids_)

            # look for nodes that found kids
            if kids.size > 0:
                # this level still has nodes to process
                self.compute_height(kids)
            else:
                self.done = 1


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
    myTree.compute_height(myTree.root)
    print(myTree.height)

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()

# initialize to store levels, starting with leaves and finding parents
#    list_levels = []

    # def compute_levels(self):
    #     parents = self.parent[self.leaves]
    #     # look for nodes that found root
    #     done_idx = np.where(self.parents < 0)[0]
    #     # replace that node with value of root node so that code won't choke
    #     self.parents[done_idx] = self.root
    #     self.list_levels.append(parents)
    #
    #     #check if all leaves found root
    #     if not done_idx.size == self.leaves.size:
    #         #ac stopped here
    #         print (self.list_levels)