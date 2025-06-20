from collections import deque

# Define the structure of a binary tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create the binary tree [1, 2, 3, 4, 5, 6, 7]
def create_tree():
    # Root node
    root = TreeNode(1)
    # Level 2
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # Level 3
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


# Function to perform preorder traversal with logging
def preorder_traversal(root): # DFS : Depth First Search
    if not root:
        return

    print(f"Visiting Node: {root.value}")

    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root): # DFS : Depth First Search
    if not root:
        return

    inorder_traversal(root.left)
    print(f"Visiting Node: {root.value}")
    inorder_traversal(root.right)

def postorder_traversal(root): # DFS : Depth First Search
    if not root:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(f"Visiting Node: {root.value}")

def levelorder_traversal(root): # BSF : Breath Fist Seach
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(f"Visiting Node: {node.value}")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Main execution
if __name__ == "__main__":
    # Create the tree
    root = create_tree()

    # # Preorder Traversal # DFS : Depth First Search
    # print("Starting Preorder Traversal...")
    # preorder_traversal(root)
    # print("Preorder Traversal Complete.")

    # # Inorder Traversal # DFS : Depth First Search
    # print("Starting Inorder Traversal...")
    # inorder_traversal(root)
    # print("Inorder Traversal Complete.")

    # # Postorder Traversal # DFS : Depth First Search
    # print("Starting Postorder Traversal...")
    # postorder_traversal(root)
    # print("Postorder Traversal Complete.")

    # Postorder Traversal # DFS : Depth First Search
    print("Starting level order Traversal...")
    levelorder_traversal(root)
    print("Level order Traversal Complete.")
