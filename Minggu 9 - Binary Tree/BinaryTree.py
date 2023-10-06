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
  def __init__(self, root):
    self.root = None

  def add(self, key):
    newNode = Node(key)
    sem = self.root
    if self.root == None:
      self.root = newNode
    else:
      while sem.getRight or sem.getLeft():
        sem = sem.getLeft if key < sem.getValue else sem.getRight()
      if  key < sem.getValue:
        sem.setLeft(newNode)
      else:
        sem.setRight()