class Node():
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def setRight(self, ri):
        self.right = ri

    def setLeft(self, le):
        self.left = le

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getValue(self):
        return self.key


class Tree():
    def __init__(self):
        self.root = None

    def add(self, key):
        newNode = Node(key)
        sem = self.root
        if self.contains(key):
            print('Value sudah ada di Tree, tidak boleh ada duplikat')
            return
        else:
            if self.root == None:
                self.root = newNode
            while sem.getRight() or sem.getLeft():
                sem = sem.getLeft() if key < sem.getValue() else sem.getRight()
            if key < sem.getValue():
                sem.setLeft(newNode)
            else:
                sem.getRight(newNode)

    def contains(self, key):
        sem = self.root
        while sem:
            if key == sem.getValue():
                return True
            sem = sem.getLeft() if key < sem.getValue() else sem.getRight()
        return False
