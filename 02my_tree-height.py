# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #9
#   modified original function computeHeight
#   array instead of list, recursive compute; looking at leaf nodes only
# results
#   Failed case #22/24: time limit exceeded
#   Time used: 6.12/3.00, memory used: 1149603840/536870912.



import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = np.array(sys.stdin.readline().split(), int)

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

            if np.where(parents_clean==-1)[0]==0 and parents_clean.size==1:
                self.done = 1
            else:
                parents_clean = parents_clean[parents_clean != -1]

                self.compute_height(parents_clean)

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
    myTree.compute_height(myTree.leaves)
    print(myTree.height)


threading.Thread(target=main).start()

