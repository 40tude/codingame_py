# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
# http://www.openbookproject.net/books/pythonds/Trees/ParseTree.html
# If the current token is a '(' or '[' add a node as a child of the current node and descend to the created child
# If the current token is a number, add the value to the list of Resistors 
# If the current token is a ')' or ']' go to the parent of the current node.  

import sys

# -----------------------------------------------------------------------------
class Node:
  def __init__(self, token):
    self.Op = token             # Serial '(' or Parallel '['
    self.Resistors = []         # Each node can have 2 or more resistors
    self.SubTrees = []          # One or more subtrees
    self.Req = 0.0
    
# -----------------------------------------------------------------------------
def BuildParseTree(Expression, Dic):
  Token = Expression.pop(0)
  Tree = Node(Token)
  CurrentTree = Tree
  
  Stack = []
  Stack.append(Tree)

  for i in Expression:
    if i in ['(', '[']:
        CurrentTree.SubTrees.append(Node(i))          # the last elements holds a reference to the new node
        Stack.append(CurrentTree)
        CurrentTree = CurrentTree.SubTrees [-1:][0]  # CurrentTree is the last element of the list of SubTrees
    elif i in [')', ']']:
      tmp = 0.0
      if i==']':
        # Add, in parallel, the Req of the sub-trees and the resistors of the branch. 
        for child in CurrentTree.SubTrees:
          tmp = tmp + 1/child.Req
        for r in CurrentTree.Resistors:
          tmp = tmp + 1/r
        CurrentTree.Req = 1/tmp
      else:
        # Add, the Req of the sub-trees and the resistors of the branch. 
        for child in CurrentTree.SubTrees:
          tmp = tmp + child.Req
        tmp = tmp + sum(CurrentTree.Resistors)
        CurrentTree.Req = tmp  
      CurrentTree = Stack.pop()
    else:
      CurrentTree.Resistors.append(Dic[i])
  return Tree

# -----------------------------------------------------------------------------
def main():
  RedirectIOtoFile = True
  if RedirectIOtoFile :
    sys.stdin = open("input4.txt", "r")

  n = int(input())
  Dico = {}  
  for i in range(n):
      inputs = input().split()
      Dico[inputs[0]] = int(inputs[1])

  Expression = input().split()

  if RedirectIOtoFile :
    sys.stdin.close()

  Circuit = BuildParseTree(Expression, Dico)
  print(f'{Circuit.Req:.1f}')

# -----------------------------------------------------------------------------
if __name__ == '__main__':
   main()