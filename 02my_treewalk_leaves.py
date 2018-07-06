# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 2: Tree Height
#   given: #of nodes and parents index
#   compute tree height, using recursion
#
# submission #14
#   modified original function computeHeight
# summary:
#   looking at leaves only, tracking visited nodes by computing their height
# results
#   Good job! (Max time used: 0.94/3.00, max memory used: 120094720/536870912.)
#
# last change: not using list comprehension; tracking height of visited nodes


import sys, threading
import time #to track time
import numpy as np

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:

    def read(self):
        # given:
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

        # hardcoded examples
        # ex1
        #self.n = 5
        #temp = '-1 0 4 0 3' # '4 -1 4 1 1'  #
        # ex2
        #self.n = 10
        #temp = '8 8 5 6 7 3 1 6 -1 5'
        #self.parent =list(map(int, temp.split()))

        # index
        self.idx = list(range(self.n))
        # find leaves
        self.leaves = list(set(self.idx) - set(self.parent))
        # keep track of each visited node & its height
        self.node_visited = [0] * self.n

    def compute_node_height(self, node):
        # get parent
        parent = self.parent[node]

        # if root
        if parent == -1:
            return 1
        # if already visited
        if self.node_visited[node]:
            return self.node_visited[node]

        # if not visited, compute its height and add to visited nodes
        self.node_visited[node] = 1 + self.compute_node_height(parent)

        return self.node_visited[node]

    # my recursive function - only look at leaves
    def compute_height(self):

        # look at leaves only
        for vertex in self.leaves:
            self.compute_node_height(vertex)

        return max(self.node_visited)

        # not using list comprehension, if did
        # return max([ self.compute_node_height(i) for i in self.leaves])

    # my recursive function1 - only look at leaves
    # def compute_height1(self):
    #     maxHeight = 0
    #
    #     for vertex in self.leaves:
    #         height = 0
    #         i = vertex
    #         while i != -1:
    #             height += 1
    #             i = self.parent[i]
    #         maxHeight = max(maxHeight, height);
    #     return maxHeight;
    #
    # #original recursive function
    # def compute_height0(self):
    #     # Replace this code with a faster implementation
    #     maxHeight = 0
    #
    #     for vertex in range(self.n):
    #         height = 0
    #         i = vertex
    #         while i != -1:
    #             height += 1
    #             i = self.parent[i]
    #         maxHeight = max(maxHeight, height);
    #     return maxHeight;


def main():
    # track time
    start_time = time.time()

    myTree = Tree()
    myTree.read()
    # compute tree height
    print (myTree.compute_height())

    # track time
    elapsed_time = time.time() - start_time
    print('done in ', elapsed_time)

threading.Thread(target=main).start()