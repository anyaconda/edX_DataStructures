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


import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = np.array(sys.stdin.readline().split(), int)

        # get root
        self.root = np.where(self.parent == -1)[0][0]
        # find leaves
        self.leaves = np.setdiff1d(np.arange(self.n), self.parent)

    def compute_height(self):
        height = 1

        while not (self.leaves.size == 1 and self.leaves[0]==self.root):
            height += 1
            _leaves = np.unique(self.parent[self.leaves])
            self.leaves = _leaves[_leaves != -1]
            _leaves = None

        return height

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

