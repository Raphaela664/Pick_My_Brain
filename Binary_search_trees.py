class UserDatabase:
    def __init__(self):
        self.users=[]
    def insert_user(self,user):
        i=0;
        while i < len(self.users):
            if user.username < self.users[i].username:
                i+=1
                break
        self.users.insert(i, user)

class TreeNode():
    def __init__(self,key):
        self.key,self.left,self.right=key,key.left,key.right

#count_levels
    def tree_height(node):
        if node is None:
            return 0
        return 1+ max(tree_height(node.left),tree_height(node.right))
#count number of nodes
    def tree_size(node):
        if node is None:
            return 0
        return 1+ tree_size(node.left)+tree_size(node.right)


