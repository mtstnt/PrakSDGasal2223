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
    
    def delete(self, value:int):
        self.root = self.__delete(self.root, value)

    def __delete(self, node:Node, value:int):
        #1. BST deletion
        if not node:
            return node
        elif value < node.val:
            node.left = self.__delete(node.left, value)
        elif value > node.val:
            node.right = self.__delete(node.right, value)
        else: #value == node.val
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.getMinValueNode(node.right)
            node.val = temp.val
            node.right = self.__delete(node.right, temp.val)

        if node is None:
            return node   
            
        #2. Update level
        node.level = 1 + max(self.getLevel(node.left), self.getLevel(node.right))
        #3. Get Balance
        balance = self.getBalance(node)
        #4. Balancing
        #left left
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)
        #right right
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)
        #left right
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        #right left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
        return node

    def getMinValueNode(self, node:Node):
        if node is None or node.left is None:
            return node
        
        return self.getMinValueNode(node.left)

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
avl.delete(20)
avl.print()
