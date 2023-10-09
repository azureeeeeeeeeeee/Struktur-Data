import random


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
        if self.root == None:
            self.root = newNode
            print(f'Berhasil insert Node bernilai {key} ke Tree!\n')
            return

        sem = self.root
        if self.contains(key):
            print(
                f'Node dengan nilai {key} sudah ada di Tree, tidak boleh ada duplikat\n')
            return
        else:
            while True:
                if key < sem.getValue():
                    if sem.getLeft() is None:
                        sem.setLeft(newNode)
                        print(
                            f'Berhasil insert Node bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getLeft()
                else:
                    if sem.getRight() is None:
                        sem.setRight(newNode)
                        print(
                            f'Berhasil insert Node bernilai {key} ke Tree!\n')
                        return
                    sem = sem.getRight()

    def contains(self, key):
        sem = self.root
        while sem:
            if key == sem.getValue():
                return True
            sem = sem.getLeft() if key < sem.getValue() else sem.getRight()
        return False

    def remove(self, key):
        def remove_node(node, key):
            if node is None:
                return node

            if key < node.getValue():
                node.setLeft(remove_node(node.getLeft(), key))
            elif key > node.getValue():
                node.setRight(remove_node(node.getRight(), key))
            else:
                if node.getLeft() is None:
                    return node.getRight()
                elif node.getRight() is None:
                    return node.getLeft()
                sem = self.find_min(node.getRight())
                node.key = sem.key
                node.setRight(remove_node(node.getRight(), sem))
            return node

        if self.contains(key):
            self.root = remove_node(self.root, key)
            print(f'Node dengan nilai {key} berhasil dihapus dari Tree!')
        else:
            print(f'Node dengan nilai {key} tidak ditemukan di Tree!')

    def find_min(self, node):
        sem = node
        while sem.getLeft():
            sem = sem.getLeft()
        return sem

    def display(self):
        def display_in_order(node):
            if node:
                display_in_order(node.getLeft())
                print(node.getValue(), end=' ')
                display_in_order(node.getRight())
        display_in_order(self.root)
        print('\n')


tree = Tree()
arr = [random.randint(1, 51) for x in range(10)]
print(arr)
for i in arr:
    tree.add(i)

print('\nNilai nilai di Node:')
tree.display()

# Menghapus Node dengan nilai 10 dan 99
tree.remove(10)
tree.remove(99)

print('\nNilai di tree setelah remove Node dengan nilai 10 dan 99:')
tree.display()
