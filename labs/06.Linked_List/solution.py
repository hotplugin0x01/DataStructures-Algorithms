#!/usr/bin/env python3

# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Single Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertatFirst(self, value):
        n = Node(value)
        n.next = self.head
        if self.head == None:
            self.tail = n
        self.head = n

    def InsertatEnd(self, value):
        if self.tail == None:
            self.InsertatFirst(value)
            return
        n = Node(value)
        self.tail.next = n
        self.tail = n

    def Insertafter(self, item, value):
        h = self.head
        while h != None:
            if h.value == item:
                n = Node(value)
                n.next = h.next
                h.next = n
                break
            h = h.next

    def DeleteatFirst(self):
        if self.head == None:
            raise Exception('Underflow! List is empty!')
        removed = self.head
        self.head = self.head.next
        del removed

    def DeleteatEnd(self):
        if self.head == None:
            raise Exception('Underflow! List is empty!')
        h = self.head
        while h.next.next != None:
            h = h.next
        removed = self.tail
        self.tail = h
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

        while h.next != None:
            if h.next.value == value:
                removed = h.next
                h.next = h.next.next
                removed.next = None
                del removed
                break
            h = h.next
        else:
            raise Exception('ValueError! Element not in List!')

    def Print(self):
        h = self.head
        while h != None:
            print(h.value)
            h = h.next


# Driver Code
obj = LinkedList()
obj.InsertatFirst(4)   # 4
obj.InsertatFirst(2)   # 2 4
obj.InsertatEnd(6)     # 2 4 6
obj.InsertatEnd(8)     # 2 4 6 8
obj.Insertafter(4, 5)  # 2 4 5 6 8
obj.Insertafter(6, 7)  # 2 4 5 6 7 8
obj.DeleteatFirst()    # 4 5 6 7 8
obj.DeleteatEnd()      # 4 5 6 7
obj.DeletebyValue(5)   # 4 6 7
obj.DeletebyValue(7)   # 4 6
obj.Print()


# Stack Using Linked List
class Stack:
    def __init__(self):
        self.list = LinkedList()

    def Push(self, value):
        self.list.InsertatEnd(value)

    def Pop(self):
        self.list.DeleteatEnd()

    def Print(self):
        self.list.Print()


# Driver Code
s = Stack()
s.Push(2)
s.Push(3)
s.Push(4)
s.Pop()
s.Print()


# Queue Using Linked List
class Queue:
    def __init__(self):
        self.list = LinkedList()

    def Enqueue(self, value):
        self.list.InsertatEnd(value)

    def Dequeue(self):
        self.list.DeleteatFirst()

    def Print(self):
        self.list.Print()


# Driver Code
q = Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Dequeue()
q.Print()