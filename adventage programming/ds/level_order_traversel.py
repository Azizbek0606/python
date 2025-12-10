class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


a8 = Node(8)
a7 = Node(7)
a6 = Node(6)
a5 = Node(5, None, a8)
a4 = Node(4)
a3 = Node(3, a6, a7)
a2 = Node(2, a4, a5)
a1 = Node(1, a2, a3)


def level_order_traversal(root, value):
    result = []
    queue = [root]
    new_node = Node(value)

    # Perform level order traversal to find insertion point
    while queue:
        current = queue.pop(0)
        result.append(current.value)

        # Check left child
        if not current.left:
            current.left = new_node
            break
        else:
            queue.append(current.left)

        # Check right child
        if not current.right:
            current.right = new_node
            break
        else:
            queue.append(current.right)

    # Verify the tree after insertion
    level_order_traversal_checker(a1)  # Start from original root


def level_order_traversal_checker(root):
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print(result)


# Test the function
print("Tree before insertion:")
level_order_traversal_checker(a1)
print("\nInserting value 9...")
level_order_traversal(a1, 9)
print("\nTree after insertion:")
level_order_traversal_checker(a1)


# def level_order_traversal(root, value):
#     result = []
#     queue = [root]
#     while len(queue) > 0:
#         if root.value == value:
#             print(True)
#             break
#         root = queue.pop(0)
#         result.append(root.value)
#         if root.left:
#             queue.append(root.left)
#         if root.right:
#             queue.append(root.right)
#
#     print(False)
#
# level_order_traversal(a1, 9)