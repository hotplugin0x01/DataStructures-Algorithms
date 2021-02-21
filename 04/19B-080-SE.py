#!/usr/bin/env python3
# coding: utf-8

import random


class Sorting:
    def __init__(self):
        self.data = []

    def GenerateRandom(self, n):
        self.data = random.sample(range(0, 100), n)
        return self.data

    def BubbleSort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data

    def Print(self):
        print(self.data)

    def InsertionSort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i-1
            while j >= 0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j = j-1
            self.data[j+1] = key
        return self.data

    def SelectionSort(self):
        n = len(self.data)
        for i in range(n-1):
            Min = i
            for j in range(i+1, n):
                if self.data[j] < self.data[Min]:
                    Min = j
            if self.data[Min] != i:
                self.data[i], self.data[Min] = self.data[Min], self.data[i]
        return self.data

    def BinarySearch(self, Value):
        l = 0
        r = len(self.data) - 1
        while l <= r:
            m = (l+r) // 2
            if Value > self.data[m]:
                l = m+1
            elif Value < self.data[m]:
                r = m-1
            else:
                return m
        return -1

    def Search(self, Value):
        for i in range(len(self.data)-1):
            if self.data[i] > self.data[i+1]:
                self.SelectionSort()
                return self.BinarySearch(Value)
        return self.BinarySearch(Value)


# DriverCode
obj = Sorting()
obj.GenerateRandom(10)
obj.Print()
obj.BubbleSort()
obj.InsertionSort()
obj.SelectionSort()
obj.Print()
print(obj.Search(8))
