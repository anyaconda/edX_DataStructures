#python 3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# After submission 7
#   after tree leaves (accurate but slow), need to improve performance
#   !forget computeHeight for now
#
#   successfully traversed - dfs, both pre-order and post-order
#   correct pre-order stacks
#   ex1.[1, 3, 4, 0, 2]
#   ex2.[8, 0, 1, 6, 3, 5, 2, 9, 7, 4]
#   correct pre-order stacks
#   ex1.[3, 0, 2, 4, 1]
#   ex2.[0, 2, 9, 5, 3, 4, 7, 6, 1, 8]

#   next: use post-order traverse to compute height
#   using python list datastruct
#   correct but way too slow
#   issue: takes a long time to build tree, aka get kids, with lists and looping
#   test tip: don't run on more than 100 nodes

import sys, threading
import time #to track time
import sys, threading
sys.setrecursionlimit(10**3) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

#define Tree class:
# given
# n is number of nodes,
# parent is the index of parent node
class Tree:
    # track traversal
    preStack = []
    postStack = []
    height = 1
    maxHeight = 0

    def read(self):
        # given:
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

        # hardcoded examples
        #ex1
        #self.n = 5  # int(sys.stdin.readline())
        #self.parent = [-1, 0, 4, 0, 3] # [4, -1, 4, 1, 1]  #
        #ex2
        #self.n = 10
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = list(map(int, temp.split()))

        #build tree
        self.idx = list(range(self.n))
        self.kids = self.setKids() #[None, [3, 4], None, None, [0, 2]]
        #self.kids = [None, [6], None, [5], None, [2, 9], [3, 7], [4], [0, 1], None]
        self.root = self.setRoot()

    def setRoot(self):
        self.root = [i for i, x in enumerate(self.parent) if x == -1]
        return self.root[0]

    def setKids(self):
        self.kids = []
        for node in self.idx:
            child_idx = [i for i, x in enumerate(self.parent) if x == node]
            #print('children found', child_idx)
            self.kids.append(child_idx)
        return self.kids

    nodeDone = False

    def computeH(self, node):
        if not self.kids[node]:
            ##self.postStack.append(node)
            self.nodeDone = True
            self.maxHeight = max(self.maxHeight, self.height)
            self.height -= 1
            return
        for kid in self.kids[node]:
            self.nodeDone = False
            ##self.TraversePostOrder(kid)
            if not self.nodeDone:
                self.height += 1
            self.computeH(kid)
        #self.postStack.append(node)
        self.nodeDone = True
        self.maxHeight = max(self.maxHeight, self.height)
        self.height -= 1

    def TraversePreOrder(self, node):
        self.preStack.append(node)
        #print('pre-order', node)

        if not self.kids[node]:
            return
        for kid in self.kids[node]:
            self.TraversePreOrder(kid)

    def TraversePostOrder(self, node):

        if not self.kids[node]:
            self.postStack.append(node)
            return
        for kid in self.kids[node]:
            self.TraversePostOrder(kid)
        self.postStack.append(node)


#---- MAIN --------
def main():
# track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()

    #print('Tree root ', myTree.root)
    #print('Tree kids ', myTree.kids)
    myTree.computeH(myTree.root)
    print (myTree.maxHeight)

    #myTree.TraversePreOrder(myTree.root)
    #print ('Pre-order traversal', myTree.preStack)

    #myTree.TraversePostOrder(myTree.root)
    #print ('Post-order traversal', myTree.postStack)

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()


