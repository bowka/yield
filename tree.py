class Node:
    def __init__(self,D,L=None,R=None):
        self.left = L
        self.right = R
        self.data = D
    
    def __repr__(self):
        return 'Vrchol('+repr(self.data)+')'
##        return self.inorder()

    def inorder(self):
        res = ''
        if self.left:
            res += self.left.inorder()
        res += repr(self.data) + ' '
        if self.right:
            res += self.right.inorder()
        return res

    
class Tree:
    def __init__(self):
        self.root = None   
        
    def add(self,new):
        if self.root == None:
            self.root = new
        else:
            actual = self.root
            
            while True:            
                if new.data == actual.data:
                    return
                
                elif actual.data > new.data:
                    if actual.left is None:
                         actual.left = new
                         return
                    else:
                        actual = actual.left
                        
                elif actual.data < new.data:
                    if actual.right is None:
                         actual.right = new
                         return
                    else:
                        actual = actual.right
                        
    def __iter__(self):
        return self.inorder()
        
    def inorder(self):
        def sub_inorder(node):
            if node.left != None:
                yield from sub_inorder(node.left)
            yield node.data
            if node.right != None:
                yield from sub_inorder(node.right)
        yield from sub_inorder(self.root)

strom = Node('a', Node('b'), Node('c'))
print(strom)

                
t = Tree()
t.root = Node(5)                
for i in range(10):
    t.add(Node(i))
##    print(t)

for node in t:
    print(node)
    
