from bridges.avl_tree_element import *

class AVLTree():
    def __init__(self, filename):
        self.nodes = []

        # read keys from txt file
        File = open(filename)
        for key in File:
            # create an AVL tree elements
            self.nodes.append(AVLTreeElement(int(key), key))
        File.close()
        # initialize the root as empty
        self.root = None
        # build the tree
        self.build()

    # build the tree
    def build(self):
        # insert node to the tree one by one
        for node in self.nodes:
            self.root = self.insert(node, self.root)

    # insert one node to current tree
    def insert(self, node, root):
        if not root:
            root = node
        # go to the left
        elif node.key < root.key:
            root.left = self.insert(node, root.left)
        # go to the right
        else:
            root.right = self.insert(node, root.right)

        # Call self.height to calculate balance factor for the root of current subtree
        # You can use something like to set the balance factor:
        #           root.balance_factor = the value of  balance factor 
       
        # Balance current subtree if root.balance_factor is greater than 1 or less than -1
        # You can use these library functions:
        #           node.key
        #           node.left
        #           node.right
        # For more library functions, please go to:
        #     http://bridgesuncc.github.io/doc/python-api/current/html/classbridges_1_1avl__tree__element_1_1_a_v_l_tree_element.html

        # your code goes here:

        # Balance Factor of each node = height of left subtree - height of right subtree
        # After each new insertion, check the balance factor of ancestors of this new node from bottom to top:
        
        root.balance_factor = self.get_balanceFactor(root)
        # if the balance factor of root of current subtree is greater than 1:
        if root.balance_factor > 1:
        # if the new inserted key is less than the left child of root:
            if node.key < root.left.key:
                self.right_rotation(root)
            else:
                self.left_rotation(root)
        # else if the balance factor of root of current subtree is less than -1:
        elif root.balance_factor < -1:
            # if the new inserted key is greater than the right child of root:
            if node.key > root.right.key:
                self.left_rotation(root)
            else:
                self.right_rotation(root)

        # recursively return root of current subtree
        return root

    def get_balanceFactor(self, node):
        return self.height(node.left) - self.height(node.right)

   # rotate to the left
    def left_rotation(self, root):
        # your code goes here:
        



        return root



    # rotate to the right
    def right_rotation(self, root):
        # your code goes here:




        return root


    # checked
    def height(self, node):
        if not node:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
        
    def root(self):
        return self.root