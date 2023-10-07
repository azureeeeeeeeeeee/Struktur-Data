class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def setLeft(self, kiri):
        self.left = kiri

    def setRight(self, kanan):
        self.right = kanan

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getKey(self):
        return self.key

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            self.insertrecursive(self.root,key)

    def insertrecursive(self, nodenow, key):
        if key < nodenow.key:
            if nodenow.getLeft() is None:
                nodenow.setLeft(Node(key))
            else:
                self.insertrecursive(nodenow.getLeft(), key)
        else:
            if nodenow.getRight() is None:
                nodenow.setRight(Node(key))
            else:
                self.insertrecursive(nodenow.getRight(), key)

    def remove(self,key):
        node = Node(key)
        if self.root:
            self.root = None

        else:
            self.removerecursive(self,key)

    def removerecursive(self, nodenow, key):
        if key < nodenow.key:
            if nodenow.getLeft(key):
                nodenow.setLeft(Node(None))
        else:
            if nodenow.getRight(key):
                nodenow.setRight(Node(None))


test = Tree()
test.insert(2)
test.insert(1)
test.remove(1)
