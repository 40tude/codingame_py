# To debug: print("Debug messages...", file=sys.stderr, flush=True)

import sys
import math

# -----------------------------------------------------------------------------
def GetNextSymbol(Circuit):
  Symbol = Circuit.pop()
  print(Symbol)
  return Circuit

# -----------------------------------------------------------------------------
def TestRecur(n):
  a=0

  if (n==0) :
    return (a)
  
  a = a+1
  return TestRecur(n-1)
  
# -----------------------------------------------------------------------------
def main():

  bob = TestRecur(2)
  print (bob)

  RedirectIOtoFile = True
  if RedirectIOtoFile :
    sys.stdin = open("input.txt", "r")

  n = int(input())
  Dico = {}  
  for i in range(n):
      inputs = input().split()
      Dico[inputs[0]] = int(inputs[1])
  
  Circuit=[]
  Circuit = input().split()
  Circuit.reverse()

  if RedirectIOtoFile :
    sys.stdin.close()

  while (len(Circuit)) :
    Circuit = GetNextSymbol(Circuit)  

# -----------------------------------------------------------------------------
if __name__ == '__main__':
   main()


# when we read a left parenthesis we are starting a new expression, 
# hence we should create a new tree to correspond to that expression. 
# 
# whenever we read a right parenthesis, we have finished an expression. 
# 
# We also know that operands are going to be leaf nodes and children of their operators. 
# every operator is going to have 2 or more childs
#
# 
# If the current token is a '(' or '[' add a new node as the child of the current node, and descend to the child.
# If the current token is a number, set the root value of the current node to the number and return to the parent.
# If the current token is a ')' or ']' go to the parent of the current node.  
# 
# [ ( A B ) [ C A ] ]
#  



# If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.