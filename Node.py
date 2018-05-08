class Node:

    def __init__(self, key=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

    def print(self):
        print(self.key)