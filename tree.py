class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    #insert function
    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            #calls private recursive insert helper func
            self._insert(data,self.root)
    
    #private recursive insert func
    def _insert(self, data, cur_node):
        #left traversal
        if data < cur_node.data:
            if cur_node.left:
                self._insert(data,cur_node.left)
            else:
                cur_node.left = node(data)
        #right traversal
        elif data > cur_node.data:
            if cur_node.right:
                self._insert(data, cur_node.right)
            else:
                cur_node.right = node(data)
        else:
            print("Data is already in the tree")
    
    #delete node from tree
    def delete(self,data):
        if self.root != None:
            self._delete(data, self.root)
    
      #findMin helper func
    def findMin(self, cur_node):
        #Now that we are on the right side of the tree
        # we need to traverse to the left to find the smallest
        # child so we can use that to replace the node we want to delete    
        if(cur_node.left != None):
            return self.findMin(cur_node.left)
        else:
            return cur_node.data

    #helper function to handle recursion 
    def _delete(self,data, cur_node):
        #traverse the tree till the data == the node we want to delete
        # left traversal 
        if data < cur_node.data:
            cur_node.left = self._delete(data, cur_node.left)
        #right traversal
        elif data > cur_node.data:
            cur_node.right = self._delete(data, cur_node.right)
        #we've found the data == the respected node
        elif data == cur_node.data:
            #Leaf Node delete
            if cur_node.left == None and cur_node.right == None:
                cur_node = None
            #one child
            elif cur_node.right != None and cur_node.left == None:
                temp = cur_node
                cur_node = cur_node.right
                temp = None
            elif cur_node.left != None and cur_node.right == None:
                temp = cur_node
                cur_node = cur_node.left
                temp = None
            #two children
            else:
                #use helper function to find the min node val on the right side of tree
                temp = self.findMin(cur_node.right)
                cur_node.data = temp
                cur_node.right = self._delete(temp, cur_node.right)
                #If the child we wanna delete has a large family below on the right side
                #We need to find the minimum node value to replace to keep the tree a BST
                #return the current node 
            return cur_node
        else:
            print("data was not in the tree")
            return

    #print tree 
    def print_tree(self):
        if self.root != None:
            #private recursive helper func
            self._print_tree(self.root)
    
    #private recursive print func
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(cur_node.data)
            self._print_tree(cur_node.right)

    #find the height of the tree
    def height_of_tree(self):
        if self.root != None:
            #private recursive func to find height
            height = self._height_of_tree(self.root)
            return height
    
    def _height_of_tree(self,cur_node):
        if cur_node == None:
            return 0
        if cur_node:
            lheight = self._height_of_tree(cur_node.left)
            rheight = self._height_of_tree(cur_node.right)
            return 1 + max(lheight, rheight)

    #func that checks if tree is balanced using a helper func
    def is_balanced(self):
        if self.root != None:
            return self._is_balanced(self.root)
        return True


    def _is_balanced(self, cur_node):
        #default edge case 
        if cur_node == None:
            return True
        #gets the height of the left subtree
        left_subTreeHeight = self._height_of_tree(cur_node.left)
        #gets the height of the right subtree
        right_subTreeHeight = self._height_of_tree(cur_node.right)
        #tree is balanced if the height of left - the height of right is <= 1
        if abs(left_subTreeHeight - right_subTreeHeight) > 1:
            return False
        #start the process over again checking the next subtrees
        lcheck = self._is_balanced(cur_node.left)
        rcheck = self._is_balanced(cur_node.right)
        #if after going through each stack both the lcheck and rcheck have return true then we are balanced
        if lcheck and rcheck:
            return True

    def level_traversal(self):
        if self.root != None: 
            self._level_traversal(self.root)
        else:
            print("tree is empty")
    
    #using a Queue to traverse tree level by level
    def _level_traversal(self, cur_node):
        #implement queue
        q = []
        #store current node to a temp
        temp_node = cur_node
        #append temp node to q
        q.append(temp_node)
        #while q is not empty we are going to 
        #pop the current node in the q and save to cur
        #cur will then have its data printed
        #then we append each child node from left to right to q and repeat process
        #till q is finally empty thus no more children to add to q
        while q:
            cur = q.pop(0)
            print(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            



        





