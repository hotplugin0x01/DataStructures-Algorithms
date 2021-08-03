class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.i = 0

    def IsEmpty(self):
        return self.i == 0
    
    def Push(self, e):
        if self.IsFull():
            raise Exception("Stack is Full!")
        self.data[self.i] = e
        self.i += 1

    def IsFull(self):
        return self.i == self.size

    def Pop(self):
        if self.IsEmpty():
            raise Exception("Stack is Empty!")
        self.i -= 1
        popped = self.data[self.i]
        return popped

    def Peek(self):
        return self.data[self.i - 1]

    def Count(self):
        return self.i

    def Print(self):
        print(self.data)


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
        self.c -= 1           # Decrementing Count
        return removed

    def Peek(self):
        return self.data[self.j]

    def Count(self):
        return self.c

    def IsEmpty(self):
        return self.c == 0

    def IsFull(self):
        return self.c == self.size

    def Print(self):
        print(self.data)
