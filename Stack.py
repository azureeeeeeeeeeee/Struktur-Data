class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def getValue(self):
        return self.value
    
class Stack:
    def __init__(self):
        self.first = None
        self.tes = 0
      
    def push(self, value):
        sem = self.first
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
        else:
            while sem.getNext():
                sem = sem.getNext()
            sem.setNext(newNode)
            self.tes +=1

    def hasPop(self):
        if self.first is None:
            return False
        else:
            return True

    def pop(self):
        sem = self.first
        prev = None

        if not self.hasPop():
            return False
        else:
            while sem.getNext():
                prev = sem
                sem = sem.getNext()
            print("Nilai yang di POP: ",sem.getValue())
            prev.setNext(sem.getNext())
            self.tes -= 1
        return True
    
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
                print('Stack Kosong')
                return None
            sem = sem.getNext()
        if sem is None:
            print('Index is out of range')
            return None
        return sem.getValue()

# Inisiasi Stack
stack = Stack()

# Mencoba Pop sebelum memasukkan data
print(stack.pop())
print('')

# Push data ke test_stack
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('1')
stack.push('2')
stack.push('3')

# Print nilai yang ada di stack
print('Nilai Nilai yang ada di stack :')
for i in range(6):
    print(stack.get(i))
print('')

# Melakukan pop di stack
stack.pop()

# Print stack setelah melakukan pop
print('Nilai nilai yang ada di stack setelah melakukan pop sebanyak 1 kali :')
for i in range(6):
    print(stack.get(i))

# Melakukan swap elemen index 1 dengan elemen index 3 
stack.swap(1, 3)

# Print nilai yang ada di queue setelah melakukan swap
print('Nilai Nilai di stack setelah sekali melakukan swap : ')
for i in range(6):
    print(stack.get(i))