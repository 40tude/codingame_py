from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def bfs(root):
    if root is None:
        return

    # Initialize a queue for BFS
    queue = deque([root])

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        # Visit the node
        print(node.val, end=" ")

        # Enqueue the left child if it exists
        if node.left:
            queue.append(node.left)
        # Enqueue the right child if it exists
        if node.right:
            queue.append(node.right)


# Create a sample binary search tree
#       50
#      /  \
#    30   70
#    / \  / \
#   20 40 60 80

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

bfs(root)  # Output: 50 30 70 20 40 60 80
