# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #10
#   modified original function computeHeight
#   array instead of list, recursive compute; starting from root and looking at kids
# results
#   Failed case #18/24: time limit exceeded
#   Time used: 6.10/3.00, memory used: 37318656/536870912.


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
        self.root = np.where(self.parent == -1)[0]


    height = 0
    done = 0
    def compute_height(self, nodes):

        while not self.done:
            self.height += 1
            #find kids
            kids = np.nonzero(np.in1d(self.parent, nodes))[0]

            # look for nodes that found kids
            if kids.size > 0:
                # this level still has nodes to process
                self.compute_height(kids)
            else:
                self.done = 1

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
    myTree.compute_height(myTree.root)
    print(myTree.height)


threading.Thread(target=main).start()

