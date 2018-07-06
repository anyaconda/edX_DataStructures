# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# after submission #10 - different strategy for case #18
# results
#   Failed case #18/24: time limit exceeded
#   Time used: 6.10/3.00, memory used: 37318656/536870912.
#
# previous: tried using np.where for ternary logic
#   start with leaves, size of array = n of leaves
#   find leaves parents (recursively), if encounter -1 set back to root node value
#   do until last level all equal root
#   count # of levels.
#   best performance so far, but short of required 3 seconds for case #22, 23
#
# here: calculating diff between nodes left and subtracting leaves
#   until left with one final node
#   great on #18 chokes on case#21, 1062 seconds; too slow on 22,23,24


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
        #temp = '4 -1 4 1 1'  # [-1, 0, 4, 0, 3] #
        # ex2
        self.n = 10
        temp = '8 8 5 6 7 3 1 6 -1 5'
        self.parent = np.array(temp.split(), int)

        self.idx = np.arange(self.n)
        self.nodes_left = self.idx

    # my recursive function - only look at leaves
    height = 1
    done = 0


    def compute_height(self):
        self.height += 1

        while not self.done:

            parents_left = self.parent[self.nodes_left]
            print('p left ', parents_left)
            leaves = np.setdiff1d(self.nodes_left, parents_left)
            print ('leaves ', leaves)
            self.nodes_left = np.setdiff1d(self.nodes_left, leaves)
            print('nodes left ', self.nodes_left)

            # look for nodes that found root
            if not self.nodes_left.size == 1:

                # check if this level still has nodes to process
                # if not done_idx.size==self.leaves.size:
                self.compute_height()
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
    myTree.compute_height()
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