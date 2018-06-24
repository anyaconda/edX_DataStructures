#python 3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# After submission 7
#   after tree leaves (accurate but slow), need to improve performance
#   try pre-order traverse
#   so far vertex.add is working, vertex.pop needs fixing

import sys, threading
import time #to track time
sys.setrecursionlimit(10**3) # max depth of recursion

#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:
    stack = []

    def read(self):
        # print('my lentth', len(self.parent))

        #self.n = int(sys.stdin.readline())
        #self.parent = list(map(int, sys.stdin.readline().split()))

        # hardcoded examples
        self.n = 5  # int(sys.stdin.readline())
        self.parent = [4, -1, 4, 1, 1]  # [-1, 0, 4, 0, 3]

        #self.n = 10
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent = list(map(int, temp.split()))

        self.me = list(range(self.n))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0

        #start with root
        root = [k for k,v in enumerate(self.parent) if v==-1]
        root_idx = root[0]

        #pre-order traversal - add parent node to stack
        Tree.stack.append(root_idx)
        print ('Starting stack', Tree.stack[len(Tree.stack) - 1])

        i = Tree.stack[len(Tree.stack) - 1]
        #call recursive function
        self.findChildIdx(i)

        return ('Not computing max height yet')

    #recursive function
    def findChildIdx(self, node_idx):
        print('stack so far:', Tree.stack)

        child_idx = [i for i, x in enumerate(self.parent) if x == node_idx]
        print('child found', child_idx)

        if len(child_idx) > 0:

            for item_idx in child_idx:
                Tree.stack.append(item_idx)
                self.findChildIdx(item_idx)

        else:
            print('no children for node ', node_idx)
            Tree.stack.pop()
            print('stack after leaves no children:', Tree.stack)


#---- MAIN --------
def main():
# track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()
    # original call to compute tree height
    print(myTree.compute_height())

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()