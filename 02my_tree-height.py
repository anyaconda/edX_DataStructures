# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:

    #--constructor
    def __init__(self, label, parent):
        self._label = label
        self._parent = parent
        self._child = []
        self._root = parent == -1

    # --setter functions
    def add_child(self, c):
        self._child.append(c)

    #traverse up each node ($actodo: keep track of seen nodes
    def traverseUp(self, this_nodes):
        me = self
        done = False

        while not done:
            if me._root:
                done = True
            else:
                ancestors.append(self._parent)
                me = this_nodes[ancestors[len(ancestors)-1]]
                me.traverseUp(this_nodes)

            return ancestors


#define Tree class: n is number of nodes, parent is the index of parent node
class TreeHeight:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))


    def build(self):
        # allocate Nodes array
        nodes = list(range(self.n))
        for i in range(0, len(nodes)):
            nodes[i] = Node(i, self.parent[i])

        # assign kids based on parents
        for child_idx in range(0, len(nodes)):
            parent_idx = nodes[child_idx]._parent
            # print (parent_idx)
            if parent_idx == -1:
                root_idx = child_idx
            else:
                nodes[parent_idx].add_child(nodes[child_idx])

        #print ('Tree built')
        return nodes

    def get_leaf_idx(self):
        # allocate Nodes array
        leaf_nodes = []
        leaf_nodes = [elem for elem in range(0,self.n) if elem not in self.parent]

        return leaf_nodes


    def compute_height(self):
        height = 0

        nodes = self.build()
        leaf_idx = self.get_leaf_idx()
        leaf_nodes = []
        leaf_nodes = [elem for elem in nodes if elem._label in leaf_idx]

        for node in leaf_nodes:
            ancestors.clear()
            ancestors.append(node._label)
            node.traverseUp(nodes)

            if len(ancestors) > height:
                height = len(ancestors)
        return height

def main():
    global ancestors
    ancestors = []
    myTree = TreeHeight()
    myTree.read()
    #print(myTree.parent)
    #was print(tree.compute_height())

    # traverseUp with class Node
    print(myTree.compute_height())


threading.Thread(target=main).start()

