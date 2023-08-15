class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev
    
    def getValue(self):
        return self.value
    
class Queue:
    def __init__(self):
        self.first =  None
      
    def push(self, value):
        sem = self.first
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
        else:
            while sem.getNext():
                sem = sem.getNext()
            sem.setNext(newNode)

    def remove(self):
        if self.first is None:
            print('Queue is empty')
        else:
            self.first = self.first.getNext()

    def swap(self, index1, index2):
        if index1 == index2:
            print('Karena index 1 dan index 2 sama, tidak ada yang berubah')
            return

        prev1 = None
        sem1 = self.first
        for i in range(index1):
            if sem1 is None:
                print('Index 1 is out of range')
                return
            prev1 = sem1
            sem1 = sem1.getNext()

        prev2 = None
        sem2 = self.first
        for i in range(index2):
            if sem2 is None:
                print('Index 2 is out of range')
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
        sem2.setNext(sem1_next)

    def get(self, index):
        sem = self.first
        for i in range(index):
            if sem is None:
                print('Queue Kosong')
                return
            sem = sem.getNext()
        if sem is None:
            print('Index is out of range')
            return
        return sem.getValue()

# Inisiasi Queue
queue = Queue()

# Remove elemen queue saat queue masih kosong
queue.remove()
print('')

# Menambahkan elemen di Queue
queue.push(1)
queue.push(2)
queue.push(3)
queue.push('A')
queue.push('B')
queue.push('C')

# Print semua nilai yang ada Queue
print('Nilai yang ada di Queue :')
for i in range(6):
    print(queue.get(i))
print('')

# Menghapus satu nilai di awal queue
queue.remove()

# Print nilai yang ada di queue setelah melakukan remove
print('Nilai Nilai di queue setelah sekali melakukan remove')
for i in range(6):
    print(queue.get(i))
print('')

# Swap nilai pada index 1 dan 3
queue.swap(1, 3)

# Print nilai yang ada di queue setelah melakukan swap
print('Nilai Nilai di queue setelah sekali melakukan swap : ')
for i in range(6):
    print(queue.get(i))