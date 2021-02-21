#!/usr/bin/env python3

# A
class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.i = 0

    def IsEmpty(self):
        if self.i == 0:
            return True
        return False

    def Push(self, e):
        if self.IsFull():
            raise Exception("Stack is Full!")
        self.data[self.i] = e
        self.i += 1

    def IsFull(self):
        if self.Count() == self.size:
            return True
        return False

    def Pop(self):
        if self.IsEmpty():
            raise Exception("Stack is Empty!")
        self.i -= 1
        popped = self.data[self.i]
        self.data[self.i] = 0
        return popped

    def Peek(self):
        return self.data[self.i - 1]

    def Count(self):
        return self.i

    def Print(self):
        print(self.data)


# B
class Queue:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.i = 0   # Enqueue Pointer
        self.j = 0   # Dequeue Pointer
        self.c = 0   # Counter variable

    def Enqueue(self, e):
        if self.IsFull():
            raise Exception("Queue is full!")
        self.data[self.i] = e
        self.i = (self.i + 1) % self.size     # Achieving Circular Array Behavior
        self.c += 1           # Incrementing Count

    def Dequeue(self):
        if self.IsEmpty():
            raise Exception("Queue is Empty!")
        removed = self.data[self.j]
        self.j = (self.j + 1) % self.size     # Achieving Circular Array Behavior
        self.data[self.j] = 0
        self.c -= 1           # Decrementing Count
        return removed

    def Peek(self):
        return self.data[self.j]

    def Count(self):
        return self.c

    def IsEmpty(self):
        if self.Count() == 0:
            return True
        return False

    def IsFull(self):
        if self.Count() == self.size:
            return True
        return False

    def Print(self):
        print(self.data)
        
        
# C
def StringExp(exp):
    s = Stack(len(exp))
    parans = {'{':'}', '(':')', '[':']'}
    
    for bracket in exp:
        if bracket in parans:
            s.Push(bracket)
            
        elif s.IsEmpty():
            return False
        
        else:
            last = s.Pop()
            if bracket != parans[last]: 
                    return False
    if s.IsEmpty():
        return True
    return False


# Driver Code
# Stack
s = Stack(5)
for i in range(5):
    s.Push(i)
print(s.Pop())
print(s.Peek())

# Queue
q = Queue(5)
for i in range(1,6):
    q.Enqueue(i)
print(q.Dequeue())
print(q.Peek())

# StringExp
test1 = '[()]{}{[()()]()}' # True
test2 = '[(])' # False

print(StringExp(test1))
print(StringExp(test2))