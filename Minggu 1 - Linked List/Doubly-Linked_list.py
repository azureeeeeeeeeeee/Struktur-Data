class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, nextNode):
        self.next = nextNode

    def setPrev(self, prevNode):
        self.prev = prevNode
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def getValue(self):
        return self.value
    



class DoublyLinkedList():
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
        else:
            sem = self.first
            while sem.getNext():
                sem = sem.getNext()
            sem.setNext(newNode)
    
    def insert(self, value, index):
        newNode = Node(value)
        if index == 0:
            newNode.setNext(self.first)
            self.first.setPrev(newNode)
            self.first = newNode
        else:
            sem = self.first
            for i in range(index - 1):
                if sem.getNext() is None:
                    print('Index is out of range')
                sem = sem.getNext()
            newNode.setNext(sem.getNext())
            newNode.setPrev(sem)
            if sem.getNext():
                sem.getNext().setPrev(newNode)
            sem.setNext(newNode)

    def remove(self, index):
        if index == 0:
            if self.first:
                self.first = self.first.getNext()
                if self.first:
                    self.first.setPrev(None)
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
            else:
                if sem.getNext().getNext():
                    sem.getNext().getNext().setPrev(sem)
                sem.setNext(sem.getNext().getNext())

    def swap(self, index1, index2):
        if index1 == index2:
            return

        prev1 = None
        sem1 = self.first
        for i in range(index1):
            if sem1 is None:
                print('List is empty')
                return
            prev1 = sem1
            sem1 = sem1.getNext()

        prev2 = None
        sem2 = self.first
        for i in range(index2):
            if sem2 is None:
                print('List is empty')
                return
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
        if sem2_next:
            sem2_next.setPrev(sem1)

        sem2.setNext(sem1_next)
        if sem1_next:
            sem1_next.setPrev(sem2)

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

# inisiasi linked list
test_list = DoublyLinkedList()

# menambah value ke linked list
test_list.add(10)
test_list.add(20)
test_list.add(30)

# memasukkan node ke linked list dengan index yang spesifik
test_list.insert(15, 1)

# print smeua nilai yang ada linked list
print('Node di linked list :')
for i in range(4):
    print(test_list.get(i))

# swap node dengan index 1 dan 3
test_list.swap(1, 3)

# print list setelah melakukan swap
print("Linked List setelah melakukan swap :")
for i in range(4):
    print(test_list.get(i))

# mengahapus node dengan index 2
test_list.remove(2)

# print linked list setelah melakukan remove
print("Linked List setelah melakukan remove :")
for i in range(3):
    print(test_list.get(i))
