# If the current token is a '(' or '[' add a new node as the Childs of the current node, and descend to the Childs.
# If the current token is a number, set the value of the current node to the number and return to the parent.
# If the current token is a ')' or ']' go to the parent of the current node.  

import math

class Node:
  def __init__(self, token):
    self.operator = token              # Serial '(' or parallel '['
    self.operands = []                 # Each node can have 2 or more resistors
    self.Childs = []                    # Each node can have more than one Childs 
    self.Req = 0.0
  
  def Traversal(self, root):
    res = []
    if root:
      res.append(root.operator)
      res.extend(root.operands)
      res.extend(self.Traversal(root.Childs))
    return res

def BuildParseTree(Expression):
  Expression = Expression.split()
  Token = Expression.pop(0)
  Tree = Node(Token)
  CurrentTree = Tree
  
  Stack = []
  Stack.append(Tree)

  for i in Expression:
    if i in ['(', '[']:
        CurrentTree.Childs.append(Node(i))          # the last elements olds a reference to the new node
        Stack.append(CurrentTree)
        CurrentTree = CurrentTree.Childs [-1:][0]  # CurrentTree is the last element of the list of childs
    elif i in [')', ']']:
    #   if i==']':
    #     tmp = 0.0
    #     for r in CurrentTree.operands:
    #       tmp = tmp + 1/r
    #     CurrentTree.Req = 1/tmp
    #   else:
    #     CurrentTree.Req = sum(CurrentTree.operands)
      CurrentTree = Stack.pop()
    else:
      # CurrentTree.operands.append(int(i))
      CurrentTree.operands.append(i)
  return Tree


# -----------------------------------------------------------------------------
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
# http://www.openbookproject.net/books/pythonds/Trees/ParseTree.html

# Expression = "[ 10 10 ]"
# Expression = "( 10 20 )"
# Expression = "[ ( A B ) [ D E F ] ]"
# Expression = "[ ( 10 20 ) ( 30 40 ) ( 50 60 ) ]"
#Expression = "[ ( 24 8 ) [ 48 24 ] ]"
Expression = "[ ( A B ) [ C A ] ]"

root = BuildParseTree(Expression)
print(root.Traversal(root))
#print(root.Req)



