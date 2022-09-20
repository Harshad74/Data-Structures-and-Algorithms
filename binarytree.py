class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None  
        self.right=None

node0=TreeNode(3) 
node1=TreeNode(4)
node2=TreeNode(5)

node0.left=node1
node0.right=node2

tree=node0
print(tree.key)
print(tree.left.key)
print(tree.right.key)

# constructing a tree
node0=TreeNode(2) 
node1=TreeNode(3)
node2=TreeNode(5)
node3=TreeNode(1) 
node4=TreeNode(3)
node5=TreeNode(7)
node6=TreeNode(4) 
node7=TreeNode(6)
node8=TreeNode(8)

node0.left=node1
node0.right=node2
node1.left=node3
node2.left=node4
node2.right=node5
node4.right=node6
node5.left=node7
node5.right=node8

print(node5.key)
print(node5.left.key)
print(node5.right.key)


# function to create a tree
def parse_tuple(data):
    if isinstance(data,tuple) and len(data)==3:
        node=TreeNode(data[1])
        node.left=parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node=None
    else:
        node=TreeNode(data)
    return node

tree1=parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree1)
print(tree1.key)
print(tree1.left.key,tree1.right.key)

# displaying a tree
def display_keys(node,space='\t',level=0):
    if node is None:
        print(space*level+'∅')
        return 

    if node.left is None and node.right is None:
        print(space*level+str(node.key))
        return 

    display_keys(node.right,space,level+1)
    print(space*level+str(node.key))
    display_keys(node.left,space,level+1)

display_keys(node0)  


# Inorder traversal
def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left)+[node.key]+inorder_traversal(node.right)

print(inorder_traversal(node0))


# Preorder traversal
def preorder_traversal(node):
    if node is None:
        return []
    return [node.key]+preorder_traversal(node.left)+preorder_traversal(node.right)

print(preorder_traversal(node0))


# Postorder traversal
def postorder_traversal(node):
    if node is None:
        return []
    return postorder_traversal(node.left)+postorder_traversal(node.right)+[node.key]

print(postorder_traversal(node0))


# height of tree
def tree_height(node):
    if node is None:
        return 0
    return 1+max(tree_height(node.left),tree_height(node.right))

print(tree_height(node0))


# number of nodes in tree
def nodesintree(node):
    if node is None:
        return 0
    return 1+nodesintree(node.left)+nodesintree(node.right)

print(nodesintree(node0))