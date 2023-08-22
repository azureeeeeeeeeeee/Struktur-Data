class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next
    def getPrev(self):
        return  self.prev
    def setPrev(self,prevNode):
        self.prev = prevNode

    def getValue(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        newNode = Node(value)
        if not self.first:
            self.first = newNode
        else:
            sem = self.first
            while sem.getNext():
                sem = sem.getNext()
            sem.setNext(newNode)

    def addlast(self,value):
        newNode = Node(value)
        if self.last == None:
            self.first = Node
            self.last = Node
            return
        self.last.setNext(Node)
        Node.setPrev(self.last)


    def insert(self, value, index):
        newNode = Node(value)
        if index == 0:
            newNode.setNext(self.first)
            self.first = newNode
        else:
            sem = self.first
            for i in range(index - 1):
                if sem.getNext() is None:
                    print('Index out of range')
                    raise IndexError('Index is out of range')
                sem = sem.getNext()
            newNode.setNext(sem.getNext())
            sem.setNext(newNode)

    def remove(self, index):
        if index == 0:
            if self.first:
                self.first = self.first.getNext()
            else:
                print('List is Empty')
        else:
            sem = self.first
            for i in range(index - 1):
                if sem.getNext() is None:
                    print('Index is out of range')
                sem = sem.getNext()
            if sem.getNext() is None:
                print('Index is out of range')
            sem.setNext(sem.getNext().getNext())

    def swap(self, index1, index2):
        if index1 == index2:
            return

        prev1 = None
        sem1 = self.first
        for i in range(index1):
            if sem1 is None:
                print('List is empty')
            prev1 = sem1
            sem1 = sem1.getNext()

        prev2 = None
        sem2 = self.first
        for i in range(index2):
            if sem2 is None:
                print('List is empty')
            prev2 = sem2
            sem2 = sem2.getNext()

        if prev1:
            prev1.setNext(sem2)
        else:
            self.first = sem2

        if prev2:
            prev2.setNext(sem1)
        else:
            self.first = sem1

        sem1_next = sem1.getNext()
        sem2_next = sem2.getNext()

        sem1.setNext(sem2_next)
        sem2.setNext(sem1_next)

    def get(self, index):
        sem = self.first
        for i in range(index):
            if sem is None:
                print('List is empty')
                return
            sem = sem.getNext()
        if sem is None:
            print('Index is out of range')
            return
        return sem.getValue()


# Membuat objek dari class LinkedList
test_list = LinkedList()

# Menambah beberapa value ke test_list
test_list.add(10)
test_list.add(20)
test_list.add(30)

# Memasukkan sebuah value ke test_list dengan index yang spesifik
test_list.insert(15, 1)

# Display Linked List
print('Semua nilai di test_list:')
for i in range(4):
    print(test_list.get(i))

# Mengubah posisi dua buah value dengan menggunakan indexnya
test_list.swap(1, 3)

# List setelah diubah
print("test_list setelah menggunakan fungsi swap() :")
for i in range(4):
    print(test_list.get(i))

# Menghapus sebuah nilai dengan index yang spesifik
test_list.remove(2)

# List setelah menggunakan fungsi remove
print("test_list setelah menghapus sebuah nilai spesifik menggunakan fungsi remove() :")
for i in range(3):
    print(test_list.get(i))