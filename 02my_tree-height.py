# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #8
#   modified original function computeHeight
#   array instead of list, recursive compute; no longer looking at leaf nodes
# results
#   Failed case #16/24: time limit exceeded
#   Time used: 6.04/3.00, memory used: 37822464/536870912.



import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:
    height = 1
    maxHeight = 0

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = np.array(sys.stdin.readline().split(), int)
        self.root = self.setRoot()

    def setRoot(self):
        self.root = np.where(self.parent == -1)
        return self.root[0][0]

    # my recursive function - only look at leaves
    def compute_height(self, node):

        kids = np.where(self.parent == node)[0]

        if not kids.any:
            ##self.postStack.append(node)
            self.nodeDone = True
            self.maxHeight = max(self.maxHeight, self.height)
            self.height -= 1
            return
        for kid in kids:
            self.nodeDone = False
            ##self.TraversePostOrder(kid)
            if not self.nodeDone:
                self.height += 1
            self.compute_height(kid)
            # self.postStack.append(node)
        self.nodeDone = True
        self.maxHeight = max(self.maxHeight, self.height)
        self.height -= 1
        return self.maxHeight

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
    print(myTree.compute_height(myTree.root))


threading.Thread(target=main).start()

