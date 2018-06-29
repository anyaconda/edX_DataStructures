#python 3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# After submission 8
#   computeHeight
#
#   successfully traversed - dfs, both pre-order and post-order
#   correct pre-order stacks
#   ex1.[1, 3, 4, 0, 2]
#   ex2.[8, 0, 1, 6, 3, 5, 2, 9, 7, 4]
#   correct pre-order stacks
#   ex1.[3, 0, 2, 4, 1]
#   ex2.[0, 2, 9, 5, 3, 4, 7, 6, 1, 8]

#   prev: use post-order traverse to compute height
#   using python numpy array (previously list datastruct)
#   which fixed issue: takes a long time to build tree, aka get kids, with lists and looping
#   correct and faster but still too slow (case #16 took 6.04 sec)
#   test tip: ok to run on 100K nodes (for anything starting with submission 8)
#
#   here: a little clean up to shave off micros seconds in computeHeight function

import numpy as np
import time #to track time
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

#define Tree class:
# given
# n is number of nodes,
# parent is the index of parent node
class Tree:

    height = 1
    maxHeight = 0

    def read(self):
        # given:
        self.n = int(sys.stdin.readline())
        self.parent = np.array(sys.stdin.readline().split(),int)

        # hardcoded examples
        #ex1
        #self.n = 5  # int(sys.stdin.readline())
        #temp = '4 -1 4 1 1' #[-1, 0, 4, 0, 3] #
        #ex2
        #self.n = 10
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = np.array(temp.split(), int)

        #build tree
        self.root = np.where(self.parent == -1)[0][0]

    def computeHeight(self, node):
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
            ##if not self.nodeDone:
            self.height += 1
            self.computeHeight(kid)
            # self.postStack.append(node)
        self.nodeDone = True
        self.maxHeight = max(self.maxHeight, self.height)
        self.height -= 1


    # track traversal
    # preStack = []
    # postStack = []

    # def TraversePreOrder(self, node):
    #     self.preStack.append(node)
    #     #print('pre-order', node)
    #
    #     if not self.kids[node]:
    #         return
    #     for kid in self.kids[node]:
    #         self.TraversePreOrder(kid)
    #
    # def TraversePostOrder(self, node):
    #
    #     if not self.kids[node]:
    #         self.postStack.append(node)
    #         return
    #     for kid in self.kids[node]:
    #         self.TraversePostOrder(kid)
    #     self.postStack.append(node)


#---- MAIN --------
def main():
# track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()

    #print('Tree root ', myTree.root)
    #print('Tree kids ', myTree.kids)
    myTree.computeHeight(myTree.root)
    print (myTree.maxHeight)

    #myTree.TraversePreOrder(myTree.root)
    #print ('Pre-order traversal', myTree.preStack)

    #myTree.TraversePostOrder(myTree.root)
    #print ('Post-order traversal', myTree.postStack)

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()


