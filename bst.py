"""
"""


class BinaryTreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = BinaryTreeNode(val)
        else:
            parent = None
            curr_node = self.root
            while curr_node is not None:
                parent = curr_node
                if val <= curr_node.val:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            new_node = BinaryTreeNode(val)
            if val <= parent.val:
                parent.left = new_node
            else:
                parent.right = new_node

    def search(self, val):

        if self.root == None:
            return False

        currentnode= self.root
        while currentnode!=None:

            if val == currentnode.val:
                return True

            if val > currentnode.val:
                 currentnode = currentnode.right
            else:
                currentnode= currentnode.left
        return False







bst = BinarySearchTree()
bst.insert(10)
bst.insert(1)
bst.insert(12)
bst.insert(15)
bst.insert(17)
bst.insert(19)
bst.insert(30)
bst.insert(90)



print "binsary search"
print bst.search(14)
print bst.search(17)














root = BinaryTreeNode(10)
root.left = BinaryTreeNode(11)
root.right = BinaryTreeNode(12)
root.left.left = BinaryTreeNode(13)
root.left.right = BinaryTreeNode(14)
root.right.left = BinaryTreeNode(15)
root.right.right = BinaryTreeNode(16)


# In order
def in_order(r):
    if r is None:
        return
    in_order(r.left)
    print r.val
    in_order(r.right)


# Pre order
def preorder(r):
    if r == None:
        return
    print r.val
    preorder(r.left)
    preorder(r.right)





# Post order

def postorder(r):
    if r == None:
        return
    postorder(r.left)
    postorder(r.right)
    print r.val


# Level order
def level_order(r):
    q = [r]
    while len(q) != 0:
        node = q.pop(0)
        print node.val
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

in_order(bst.root)
# preorder(root)
# print "post"
# postorder(root)
# print "inorder"
# in_order(root)
# print "level"
# level_order(root)
#
# stack = []
# stack.append(10)
# stack.pop()
#
# queue = []
# queue.append(10)
# queue.pop(0)




def dfs(folder_path, file_name):
    children = get_children(folder_path)
    for child in children:
        if child == file_name:
            return True
        if is_dir(child):
            found = dfs(child, file_name)
            if found:
                return True
    return False