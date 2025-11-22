# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# def getHeight(root, h):
#     if root is None:
#         return h - 1
#     return max(getHeight(root.left, h + 1), getHeight(root.right, h + 1))

# def levelOrder(root):
#     queue = deque()
#     queue.append((root, 0))

#     lastLevel = 0
#     height = getHeight(root, 0)

#     while queue:
#         node, lvl = queue.popleft()

#         if lvl > lastLevel:
#             print()
#             lastLevel = lvl

#         if lvl > height:
#             break

#         print("N" if node.data == -1 else node.data, end=" ")

#         if node.data == -1:
#             continue

#         if node.left is None:
#             queue.append((Node(-1), lvl + 1))
#         else:
#             queue.append((node.left, lvl + 1))

#         if node.right is None:
#             queue.append((Node(-1), lvl + 1))
#         else:
#             queue.append((node.right, lvl + 1))

# def insert(root, key):
 
#     if root is None:
#         return Node(key)

#     if key < root.data:
#         root.left = insert(root.left, key)
#     else:
#         root.right = insert(root.right, key)

#     return root


# root = None
# root = insert(root, 22)
# root = insert(root, 12)
# root = insert(root, 30)
# root = insert(root, 8)
# root = insert(root, 20)
# root = insert(root, 30)
# root = insert(root, 15)

# levelOrder(root)





class Node():
    def __init__(self, value=None, endOfWord=False):
        self.value = value
        self.left = None
        self.right = None
        self.equal = None
        self.endOfWord = endOfWord
    

class Autocomplate():
    def __init__(self, word_list):
        self.n = Node()
        for word in word_list:
            self.insert(word, self.n)
        
    def insert(self, word, node):
        char = word[0]
        if not node.value:
            node.value = char
        
        if char < node.value:
            if not node.left:
                node.left = Node()
            self.insert(word, node.left)
        
        elif char > node.value:
            if not node.right:
                node.right = Node()
            self.insert(word, node.right)
        else:
            if len(word) == 1:
                node.endOfWord = True
                return

            if not node.equal:
                node.equal = Node()
            self.insert(word[1:], node.euqal)
    
    def all_suffixes(self, patter, node):
        if node.endOfWord:
            yield "{0}{1}".format(patter, node.value)
        
        if node.left:
            for word in self.all_suffixes(patter, node.left):
                yield word
        
        if node.right:
            for word in self.all_suffixes(patter, node.right):
                yield word
        
        if node.equal:
            for word in self.all_suffixes(patter + node.value, node.equal):
                yield word
            
    def find(self, pattern):
        final_pattern = {pat: set([]) for pat in pattern}
        for pat in final_pattern.keys():
            word = self.find_(pat)
            if word == None:
                return None
            else:
                completison = {x for x in word}
            return list(completison)

    def find_(self, pattern):
        node = self.n
        for char in pattern:
            while True:
                if char > node.value:
                    node = node.right
                elif char < node.value:
                    node = node.left
                else:
                    node = node.equal
                    break
                if not node:
                    return None
        return self.all_suffixes(pattern, node)

pattern = ["c"]
word_list = [
    'aardvard',
    'altimeter'
]