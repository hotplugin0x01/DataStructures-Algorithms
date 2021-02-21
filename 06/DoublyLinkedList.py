#!/usr/bin/env python


# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


# Doubly or Double Linked List
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def InsertatFirst(self, value):
        n = Node(value)
        n.next = self.head
        if self.head == None:
            self.tail = n
        else:
            self.head.previous = n
        self.head = n
        
    def InsertatEnd(self, value):
        if self.tail == None:
            self.InsertatFirst(value)
            return
        
        n = Node(value)
        self.tail.next = n
        n.previous = self.tail
        self.tail = n
        
    def Insertafter(self, item, value):
        h = self.head
        while h != None:
            if h.value == item:
                n = Node(value)
                n.previous = h
                h.next = n
                break
            h = h.next
            
    def DeleteatFirst(self):
        if self.head == None:
            raise Exception('Underflow! List is empty!')
        removed = self.head
        self.head = self.head.next
        if self.head != None:
            self.head.previous = None
            removed.next = None
        del removed
        
    def DeleteatEnd(self):
        if self.tail == None:
            raise Exception('Underflow! List is empty!')
        removed = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        del removed
    
    def DeletebyValue(self, value):
        h = self.head
        
        if h.value == value:
            self.DeleteatFirst()
            return
        elif self.tail.value == value:
            self.DeleteatEnd()
            return
        
        while h != None:
            if h.value == value:
                removed = h.value
                h.previous.next = h.next
                h.next.previous = h.previous
                h.previous = None
                h.next = None
                del removed
                break
            h = h.next
            
    def Print(self):
        h = self.head
        while h != None:
            print(h.value)
            h = h.next


# Driver Code
obj = DoubleLinkedList()
for i in range(1, 5):
    obj.InsertatFirst(i)
    obj.InsertatEnd(i+1)
for i in range(3):
    obj.DeleteatFirst()
for i in range(2):
    obj.DeleteatEnd()
obj.DeletebyValue(1)
obj.DeletebyValue(3)
obj.Insertafter(2,3)
obj.Insertafter(3,4)
obj.Print()

