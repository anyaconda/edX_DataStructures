# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #11
#   modified original function computeHeight
#   looking at leaves only
# results
#   Failed case #22/24: time limit exceeded
#   Time used: 6.51/3.00, memory used: 56582144/536870912


import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = np.array(sys.stdin.readline().split(), int)

        # find leaves
        self.leaves = np.setdiff1d(np.arange(self.n), self.parent)

    height = 0
    done = 0

    def compute_height(self):

        while not self.done:
            self.height += 1
            self.leaves = np.where(self.leaves > -1, self.parent[self.leaves], -1)

            # look for nodes that still have parents
            if not np.all(self.leaves == -1):
                self.compute_height()
            else:
                self.done=1

        return self.height

    # original from starter solution
    # def compute_height(self):
    #     # Replace this code with a faster implementation
    #     maxHeight = 0
    #     for vertex in range(self.n):
    #         height = 0
    #         i = vertex
    #         while i != -1:
    #             height += 1
    #             i = self.parent_idx[i]
    #         maxHeight = max(maxHeight, height);
    #     return maxHeight;

def main():
    myTree = Tree()
    myTree.read()
    print(myTree.compute_height())


threading.Thread(target=main).start()

