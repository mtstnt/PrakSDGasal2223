class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.level = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        self.root = self.__insert(self.root, val)

    def __insert(self, node: Node, val: int):
        #1. insert normal BST
        if not node:
            return Node(val)
        elif val > node.val:
            node.right = self.__insert(node.right, val)
        else:
            node.left = self.__insert(node.left, val)

        #2. update level node
        node.level = 1 + max(self.getLevel(node.left), self.getLevel(node.right))
        #3. check balance
        balance = self.getBalance(node)
        #4. update tree, balancing
        #left left
        if balance > 1 and val < node.left.val:
            return self.rightRotate(node)
        #right right
        elif balance < -1 and val > node.right.val:
            return self.leftRotate(node)
        #left right
        elif balance > 1 and val > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        #right left
        elif balance < -1 and val < node.right.val:
            node.right = self.rightRotate(node.roght)
            return self.leftRotate(node)

        return node

    def leftRotate(self, a:Node):
        b = a.right
        c = b.left

        #rotate left
        b.left = a
        a.right = c

        #update level
        a.level = 1 + max(self.getLevel(a.left), self.getLevel(a.right))
        b.level = 1 + max(self.getLevel(b.left), self.getLevel(b.right))

        return b


    def rightRotate(self, a:Node):
        b = a.left
        c = b.right

        #rotate right
        b.right = a
        a.left = c

        #update level
        a.level = 1 + max(self.getLevel(a.left), self.getLevel(a.right))
        b.level = 1 + max(self.getLevel(b.left), self.getLevel(b.right))

        return b

    def getLevel(self, node: Node):
        if not node:
            return 0

        return node.level

    def getBalance(self, node:Node):
        if not node:
            return 0

        return self.getLevel(node.left) - self.getLevel(node.right)

    def print(self):
        self.__print(self.root)
        print()
    
    def __print(self, node: Node):
        if not node:
            return
        self.__print(node.left)
        print("{0}({1})".format(node.val, node.level), end=" ")
        self.__print(node.right)


avl = AVLTree()
avl.insert(10)
avl.print()
avl.insert(20)
avl.print()
avl.insert(30)
avl.print()
avl.insert(50)
avl.print()
avl.insert(15)
avl.print()
