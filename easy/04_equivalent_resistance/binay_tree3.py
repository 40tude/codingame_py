# If the current token is a '(' or '[' add a node as a child of the current node and descend to the created child
# If the current token is a number, add the value to the list of operands 
# If the current token is a ')' or ']' go to the parent of the current node.  

import sys

class Node:
  def __init__(self, token):
    self.operator = token              # Serial '(' or parallel '['
    self.operands = []                 # Each node can have 2 or more resistors
    self.Childs = []
    self.Req = 0.0

  def Traversal(self):
    res = []
    if self:
      res.append(self.operator)
      res.extend(self.operands)
      for child in self.Childs:
        res.extend(child.Traversal())
    return res
    
  def Solve(self):
    Val = 0.0
    return Val

def BuildParseTree(Expression, Dic):
  # Expression = Expression.split()
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
      if i==']':
        tmp = 0.0
        for r in CurrentTree.operands:
          tmp = tmp + 1/r
        CurrentTree.Req = 1/tmp
      else:
        CurrentTree.Req = sum(CurrentTree.operands)
      CurrentTree = Stack.pop()
    else:
      CurrentTree.operands.append(Dic[i])
  return Tree


# -----------------------------------------------------------------------------
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
# http://www.openbookproject.net/books/pythonds/Trees/ParseTree.html



RedirectIOtoFile = True
if RedirectIOtoFile :
  sys.stdin = open("input3.txt", "r")

n = int(input())
Dico = {}  
for i in range(n):
    inputs = input().split()
    Dico[inputs[0]] = int(inputs[1])


# Expression = "[ 10 10 ]"
# Expression = "( 10 20 )"
# Expression = "[ ( A B ) [ D E F ] ]"
# Expression = "[ ( 10 20 ) ( 30 40 ) ( 50 60 ) ]"

# Expression=[]
Expression = input().split()

if RedirectIOtoFile :
  sys.stdin.close()

root = BuildParseTree(Expression, Dico)
print(root.Traversal())

print(root.Solve())




