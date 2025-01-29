class Node:
  def __init__(self, Value):
    self.left = None
    self.right = None
    self.Value = Value

  # Insert Node
  def insert(self, Value):
    if self.Value:
        if Value < self.Value:
          if self.left is None:
              self.left = Node(Value)
          else:
              self.left.insert(Value)
        elif Value > self.Value:
          if self.right is None:
              self.right = Node(Value)
          else:
            self.right.insert(Value)
    else:
      self.Value = Value
  
  # Print the Tree
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print( self.Value),
    if self.right:
      self.right.PrintTree()

  # Postorder traversal Left -> Right -> Root
  def PostorderTraversal(self, root):
    res = []
    if root:
      res = self.PostorderTraversal(root.left)
      res = res + self.PostorderTraversal(root.right)
      res.append(root.Value)
    return res




# -----------------------------------------------------------------------------
# https://www.tutorialspoint.com/python_Value_structure/python_binary_tree.htm
# http://www.openbookproject.net/books/pythonds/Trees/ParseTree.html
root = Node(27)
root.insert(14)
root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
root.PrintTree()
print(root.PostorderTraversal(root))