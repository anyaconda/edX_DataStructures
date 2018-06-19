# python3
"""
# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#   only looking at leaf nodes - less memory but still time limit exceeded
"""

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent_idx = list(map(int, sys.stdin.readline().split()))


    def leaf_idx(self):
        # allocate Nodes array
        leaf_idx = []
        leaf_idx = [elem for elem in range(0, self.n) if elem not in self.parent_idx]

        return leaf_idx

    #track max
    max_height = 0

    # traverse up each node - recursive
    def traverseNodeUp(self, n_idx):
        node_parent_idx = self.parent_idx[n_idx]

        if node_parent_idx!=-1:
            ancestors.append(node_parent_idx)
            self.traverseNodeUp(node_parent_idx)

        return len(ancestors)

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
    #declare global and local variables
    global ancestors
    ancestors = []
    max_height = 0
    height = 0

    #read in tree
    myTree = Tree()
    myTree.read()
    #find leaves only
    tree_leaves = myTree.leaf_idx()

    #get height of every leaf (recursive)
    for n_idx in tree_leaves:
        ancestors.clear()
        ancestors.append(n_idx)
        height = myTree.traverseNodeUp(n_idx)
        #get max
        max_height = max(height, max_height)

    print(max_height)


threading.Thread(target=main).start()

