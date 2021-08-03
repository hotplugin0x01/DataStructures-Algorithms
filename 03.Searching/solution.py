#!/usr/bin/env python3
# coding: utf-8


# A
def LinearSearch(List, Value):
    for i in range(len(List)):
        if List[i] == Value:
            return i
    return -1

# Driver Code
data = [1,2,3,4,5]
print(LinearSearch(data, 6))


# B
def BinarySearch(List, n, Value):
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        
        if List[m] < Value:
            l = m + 1
        
        elif List[m] > Value:
            r = m - 1
            
        else:
            return m
    return -1

# Driver Code
data = [1,2,3,4,5,6,7,8,9]
n = len(data)
value = 3
print(BinarySearch(data, n, value))



# C
class List:
    def __init__(self):
        self.data = []

    
    def InsertAtFirst(self, value):
        self.data.insert(0, value)
        
    def InsertAtEnd(self, value):
        self.data.append(value)
        
    def DeleteFromFirst(self):
        deleted = self.data[0]
        self.data = self.data[1:]
        return deleted
        
    def DeleteFromEnd(self):
        deleted = self.data[-1]
        self.data = self.data[:-1]
        return deleted
        
    def LinearSearch(self, Value):
        for i in range(len(self.data)):
            if self.data[i] == Value:
                return i
        return -1
    
    def BinarySearch(self, Value):
        l = 0
        r = len(self.data) - 1
        while l <= r:
            m = (l + r) // 2

            if self.data[m] < Value:
                l = m + 1

            elif self.data[m] > Value:
                r = m - 1

            else:
                return m
            
        return -1
    
    def IsSorted(self):
        for i in range(len(self.data)-1):
            if self.data[i] > self.data[i+1]:
                return False
        return True
        
    def Search(self, Value):
        if self.IsSorted():
            return self.BinarySearch(Value)
        else:
            return self.LinearSearch(Value)


# Driver Code
obj = List()
obj.InsertAtFirst(1)
obj.InsertAtFirst(3)
obj.InsertAtFirst(6)
obj.InsertAtEnd(8)
obj.InsertAtEnd(5)
obj.InsertAtEnd(7)

print(obj.DeleteFromFirst())
print(obj.DeleteFromEnd())
print(obj.Search(8))

