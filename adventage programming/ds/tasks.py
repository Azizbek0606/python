class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a8 = Node('8')
a7= Node('7')
a6= Node('6')
a5= Node('5',None, a8)
a4= Node('4')
a3= Node('3',a6,a7)
a2= Node('2',a4,a5)
a1= Node('1', a2,a3)


# def find_biggest(root):
#     if root is None:
#         return '0'
#
#     current = root.value
#     left = find_biggest(root.left)
#     right = find_biggest(root.right)
#
#     return max(current, left, right)
#
#
def deepest_path(root):
    if root is None:
        return [], 0

    left_path, left_depth = deepest_path(root.left)
    right_path, right_depth = deepest_path(root.right)

    if left_depth > right_depth:
        return [root.value] + left_path, left_depth + 1
    else:
        return [root.value] + right_path, right_depth + 1


# print(deepest_path(a1))


def BT_min(root):
    if root is None:
        return None

    left = BT_min(root.left)
    right = BT_min(root.right)
    current = root.value
    if left is not None:
        current = min(left, current)
    if right is not None:
        current = min(right, current)
    return current

# print(BT_min(a1))
import copy

def deepest_path_tree(root, lst):
    if root is None:
        return lst

    lst.append(root.value)
    left_lst = copy.deepcopy(lst)
    right_lst = copy.deepcopy(lst)

    left_path = deepest_path_tree(root.left, left_lst)
    right_path = deepest_path_tree(root.right, right_lst)

    if len(left_path) > len(right_path):
        return left_path
    return right_path

a = deepest_path_tree(a1,[])
b = " -> ".join(a)
print(b)


