from Node import Node
import pprint as pp

class BinaryTree:

    def __init__(self, root=None, val=None):
        self.root = None
        if root == None and val == None:
            root = Node()
        elif root == None and val != None:
            self.root = Node(val)
        elif root != None:
            self.root = root
    
    def insert(self, root, node):
        if root == None:
            root = node
        if root.key < node.key:
            if root.right != None:
                self.insert(root.right, node)
            else:
                root.right = node
        elif root.key > node.key:
            if root.left != None:
                self.insert(root.left, node)
            else:
                root.left = node
    
    def printTree(self, node):
        # VLR
        if node == None:
            return
        node.print()
        self.printTree(node.left)
        self.printTree(node.right)

    @classmethod
    def calcHeight(cls, node):
        if node == None:
            return 0
        else:
            return 1 + max(BinaryTree.calcHeight(node.left), 
            BinaryTree.calcHeight(node.right))
    
    @classmethod
    def buildTree(cls):
        binTree = BinaryTree(Node(18))
        binTree.insert(binTree.root, Node(9))
        binTree.insert(binTree.root, Node(7))
        binTree.insert(binTree.root, Node(11))
        binTree.insert(binTree.root, Node(27))
        binTree.insert(binTree.root, Node(25))
        binTree.insert(binTree.root, Node(36))
        binTree.insert(binTree.root, Node(37))
        binTree.insert(binTree.root, Node(38))
        binTree.insert(binTree.root, Node(39))
        binTree.insert(binTree.root, Node(360))
        return binTree

    @classmethod
    def BFS(cls, node):
        if node != None:
            if node.key != None:
                print(node.key)
            if node.left != None:
                BinaryTree.BFS(node.left)
            if node.right != None:
                BinaryTree.BFS(node.right)



if __name__ == '__main__':
    tree = BinaryTree.buildTree()
    height = BinaryTree.calcHeight(tree.root)
    print(BinaryTree.BFS(tree.root))