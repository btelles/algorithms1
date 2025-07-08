

class BinarySearchTree():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self):
    return "(d: %s  l: %s r: %s)\n" % (self.data, self.left, self.right)

  def add(self,data):
    # Ignore same values
    if data == self.data:
      return
    
    # Go left
    if data < self.data:
      if self.left:
        self.left.add(data)
      else:
        self.left = BinarySearchTree(data)
      
    # Go right
    if self.data < data:
      if self.right:
       self.right.add(data)
      else:
        self.right = BinarySearchTree(data)

  def search(self, data):
    if self.data == data:
      return self.data
 
    if data < self.data and self.left:
      return self.left.search(data)

    if self.data < data and self.right:
      return self.right.search(data)

    return None


a = BinarySearchTree(100)
a.add(1000)
a.add(20)
a.add(200)
a.add(10)
a.add(2000)

print(a)

print(f"a.search(200): {a.search(200)}")
print(f"a.search(1000): {a.search(1000)}")
print(f"a.search(201): {a.search(201)}")



