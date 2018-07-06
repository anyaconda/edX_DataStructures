# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #14
#   modified original function computeHeight
#   looking at leaves only, tracking visited nodes by computing their height
# results
#   Good job! (Max time used: 0.94/3.00, max memory used: 120094720/536870912.)


import sys, threading
import numpy as np
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


#define Tree class: n is number of nodes, parent is the index of parent node
class Tree:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

        # index
        self.idx = list(range(self.n))
        # find leaves
        self.leaves = list(set(self.idx) - set(self.parent))
        # keep track of each visited node & its height
        self.node_visited = [0] * self.n

    def compute_node_height(self, node):
        #get parent
        parent = self.parent[node]

        #if root
        if parent== -1:
            return 1
        #if already visited
        if self.node_visited[node]:
            return self.node_visited[node]

        #if not visited, compute its height and add to visited nodes
        self.node_visited[node] = 1 + self.compute_node_height(parent)

        return self.node_visited[node]

    def compute_height(self):
        # look at leaves only
        for vertex in self.leaves:
            self.compute_node_height(vertex)

        return max(self.node_visited)

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

