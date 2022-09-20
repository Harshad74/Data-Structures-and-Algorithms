# Program to check whether a binary tree is binary search tree or not
def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True,None,None

    is_bst_l,min_l,max_l=is_bst(node.left)
    is_bst_r,min_r,max_r=is_bst(node.right)

    is_bst_node=(is_bst_l and is_bst_r and (max_l is None or node.key>max_l) and (min_r is None or node.key<min_r))

    min_key=min(remove_none([min_l,node.key,min_r]))
    max_key=max(remove_none([max_l,node.key,max_r]))

    return is_bst_node,min_key,max_key


class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
        print('user created')

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self,guest_name):
        print(f'Hi {guest_name}, I am {self.name}! contact me at {self.email}')


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


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


class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

display_keys(tree)

def find(node,key):
    if node is None:
        return None
    if key==node.key:
        return node
    if key>node.key:
        return find(node.right,key)
    if key<node.key:
        return find(node.left,key)

print((find(tree,'hemanth')).key,(find(tree,'hemanth')).value)


def update(node,key,value):
    target=find(node,key)
    if target is not None:
        target.value=value

update(tree,'hemanth',User('hemanth','Hemanth J','hemanthj@example.com'))
node=find(tree,'hemanth')
print(node.value)

def list_all(node):
    if node is None:
        return []
    return list_all(node.left)+[node.key,node.value]+list_all(node.right)

print(list_all(tree))


def is_balanced(node):
    if node is None:
        return True,0
    is_balanced_l,height_l=is_balanced(node.left)
    is_balanced_r,height_r=is_balanced(node.right)

    balanced=(is_balanced_l and is_balanced_r) and abs(height_l - height_r)<=1
    height=1+max(height_l,height_r)
    return balanced,height

print(is_balanced(tree))
