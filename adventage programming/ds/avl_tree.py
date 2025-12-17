class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.height = 0
        self.left = left
        self.right = right


a9 = Node(9)
a8 = Node(8, None, a9)
a7 = Node(7)
a6 = Node(6)
a5 = Node(5, None, a8)
a4 = Node(4)
a3 = Node(3, a6, a7)
a2 = Node(2, a4, a5)
a1 = Node(1, a2, a3)


def is_balanced(root):
    if root is None:
        return True, 0

    left,l_count = is_balanced(root.left)
    right,r_count = is_balanced(root.right)
    print(left,right,l_count,r_count)
    return left and right, abs(l_count - r_count) + 1

print(is_balanced(a1))