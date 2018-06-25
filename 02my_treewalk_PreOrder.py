#python 3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# After submission 7
#   after tree leaves (accurate but slow), need to improve performance
#   forget computeHeight for now
#
#   print pre-order traverse - verbose
#   correct pre-order stacks
#   ex1.[1, 3, 4, 0, 2]
#   ex2.[8, 0, 1, 6, 3, 5, 2, 9, 7, 4]

import sys, threading
import time #to track time
sys.setrecursionlimit(10**3) # max depth of recursion

#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:
    # track pre-order traversal
    preStack = []
    moreChildren = 1

    def read(self):
        # print('my lentth', len(self.parent))

        #self.n = int(sys.stdin.readline())
        #self.parent = list(map(int, sys.stdin.readline().split()))

        # hardcoded examples
        #ex1
        self.n = 5  # int(sys.stdin.readline())
        self.parent = [4, -1, 4, 1, 1]  # [-1, 0, 4, 0, 3]

        #ex2
        #self.n = 10
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = list(map(int, temp.split()))

        self.me = list(range(self.n))

    def printPreorder(self):
        print ('print tree pre-order traversal')

        # start with root - must be one root only!
        root = [k for k, v in enumerate(self.parent) if v == -1]
        root_idx = root[0]
        Tree.preStack.append(root_idx)
        print('Starting stack', Tree.preStack)

        i = Tree.preStack[len(Tree.preStack) - 1]

        while Tree.moreChildren:
            # call recursive function
            i = self.preOrderTraverse(i)

        print (Tree.preStack)


    def preOrderTraverse(self, node_idx):
        print('stack so far:', Tree.preStack)
        child_idx = [i for i, x in enumerate(self.parent) if x == node_idx]
        print('child found', child_idx)

        if len(child_idx) > 0:

            for item_idx in child_idx:
                Tree.preStack.append(item_idx)
                self.preOrderTraverse(item_idx)

        else:
            print('no children for node ', node_idx)
            print('stack after leaves no children:', Tree.preStack)
            Tree.moreChildren = 0



#---- MAIN --------
def main():
# track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()
    myTree.printPreorder()

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()