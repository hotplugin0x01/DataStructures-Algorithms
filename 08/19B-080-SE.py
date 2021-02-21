#!/usr/bin/env python
# coding: utf-8

# In[39]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BST:
    def __init__(self):
        self.root = None
        
    def Insert(self, v):
        self.root = self.__Insert(self.root, v)
        
    def __Insert(self, root, v):
        if root is None:
            root = Node(v)
        else:
            if v > root.data:
                root.right = self.__Insert(root.right, v)
            else:
                root.left = self.__Insert(root.left, v)
        return root
        
    # LVR = Left, Visit, Right
    def InOrder(self):
        return self.__InOrder(self.root)
        
    def __InOrder(self, root):
        if root:
            self.__InOrder(root.left)
            print(root.data)
            self.__InOrder(root.right)

    # VLR = Visit, Left, Right
    def PreOrder(self):
        return self.__PreOrder(self.root)
    
    def __PreOrder(self, root):
        if root is not None:
            print(root.data)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
       
    # LRV = Left, Right, Visit
    def PostOrder(self):
        return self.__PostOrder(self.root)
    
    def __PostOrder(self, root):
        if root is not None:
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
            print(root.data)
    
    def Height(self):
        return self.__Height(self.root)
    
    def __Height(self, root):
        if root is None:
            return -1
        left = self.__Height(root.left)
        right = self.__Height(root.right)
        height = 1 + max(left, right)
        return height
    
    def FindMin(self):
        return self.__Min(self.root).data
    
    def __Min(self, root):
        if root.left is None:
            return root
        return self.__Min(root.left)

    def FindMax(self):
        return self.__Max(self.root).data
    
    def __Max(self, root):
        if root.right is None:
            return root
        return self.__Max(root.right)

    def Successor(self):
        return self.__Successor(self.root).data
    
    def __Successor(self, n):
        return self.__Min(n.right)
    
    def Predecessor(self):
        return self.__Predecessor(self.root).data
    
    def __Predecessor(self, n):
        return self.__Max(n.left)
    
    def Search(self, v):
        return self.__Search(self.root, v)
    
    def __Search(self, n, v):
        # Check if Element not found
        if n is None:
            return -1
        elif n.data == v:
            return n
        else:
            if v < n.data:
                return self.__Search(n.left, v)
            else:
                return self.__Search(n.right, v)

    def Delete(self, v):
        if self.Search(v) != -1:
            return self.__Delete(self.root, v)
        raise Exception('Element not in tree!')
    
    def __Delete(self, n, v):
        if v > n.data:
            n.right = self.__Delete(n.right, v)
        elif v < n.data:
            n.left = self.__Delete(n.left, v)
        
        else:

            if n.right is None:
#                 print('Right is None')
                left = n.left
                n = None
#                 print(left, 'Left')
                return left

            elif n.left is None:
#                 print('Left is None')
                right = n.right
                n = None
                return right

            # If node have Children then find sucessor and replace
            NodeSuccessor = self.__Successor(n)
#             print(NodeSuccessor.data)

            n.data = NodeSuccessor.data

            # Delete the successor
            self.__Delete(n.right, NodeSuccessor.data)


# In[40]:


obj = BST()
obj.Insert(2)
obj.Insert(4)
obj.Insert(1)
obj.Insert(3)
# obj.PreOrder()
# obj.InOrder()
# obj.PostOrder()
obj.Delete(3)
obj.InOrder()


# In[ ]:




