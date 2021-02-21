#!/usr/bin/env python3
# coding: utf-8


# Q1 - a
class Array:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [0 for i in range(self.rows * self.cols)]     
        
# Q1 - b
    def Location(self, i, j):
        if self.rows > self.cols:
            return (i * self.cols + j)
        return (i * self.rows + j)

    def SetValue(self, i, j, v):
        l = self.Location(i, j)
        self.data[l] = v
        
# Q1 - c
    def GetValue(self, i, j):
        l = self.Location(i, j)
        return self.data[l]
        
# Q1 - d
    def PrintValues(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.GetValue(i, j), end=" ")
            print("\n")

# Q1 - e
    def SubValues(self, array1, array2):
        for i in range(self.rows):
            for j in range(self.cols):
                array1.data[self.Location(i, j)] -= array2.data[self.Location(i, j)]
        return array1
        
        
# Q1 - f
    def MultValues(self, array1, array2):
        if array1.cols == array2.rows:
            product = [0 for i in range(array1.rows * array2.cols)]
            for i in range(array1.rows):
                for j in range(array2.cols):
                    for k in range(array2.rows):
                        product[self.Location(i, j)] += array1.data[self.Location(i, k)] * array2.data[self.Location(k, j)]
            return product

    
# Q1 - g
    def Transpose(self):
        transpose = [0 for i in range(self.cols * self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):   
                transpose[self.Location(j, i)] = self.data[self.Location(i, j)] 
        return transpose

    
    
# Driver Code
def SettingValues(row, col, obj):
    for i in range(row):
        for j in range(col):
            obj.SetValue(i, j, i+j) 

# Array1
row = 3
col = 2
arr1 = Array(row, col)
SettingValues(row, col, arr1)

# Array2
row = 2
col = 5
arr2 = Array(row, col)
SettingValues(row, col, arr2)

# Subtraction
sub = arr1.SubValues(arr1, arr2)
sub.PrintValues()

# Mutiplication
mult = arr1.MultValues(arr1, arr2)
print(mult)

# Transpose
transpose = arr1.Transpose()
print(transpose)


# Q2-1
import numpy as np
array1 = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print(array1)


# Q2-2
x = np.ones((3,4), dtype=np.int64)
print(x)


# Q2-3
y = np.zeros((2,3,4), dtype=np.int16)
print(y)


# Q2-4
array2 = np.random.random((2,2))
print(array2)


# Q2-5
array3 = np.full((3,3), 7)
print(array3)


# Q2-6
array4 = np.identity(3, dtype=np.int64)
print(array4)


# Q2-7
add = np.add(x,y)
print(add)


# Q2-8
diff = np.subtract(x, y)
print(diff)


# Q2-9
mult = np.multiply(x, y)
print(mult)


# Q2-10
div = np.divide(y, x)
print(div)


# Q2-11
rem = np.remainder(y, x)
print(rem)


# Q2-12
result = np.array_equal(x,y)
print(result)