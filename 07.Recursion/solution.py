#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a
def Write(n):
    if n == 0:
        return
    print(n)
    Write(n-1)
    
Write(5)


# In[2]:


# b
def Factorial(n):
    if n ==1 or n==1:
        return 1
    fact = n * Factorial(n-1)
    return fact
    
print(Factorial(5))


# In[3]:


# c
def GCD(n1, n2):
    if n2 == 0:
        return n1
    return GCD(n2, n1%n2)

print(GCD(8, 12))


# In[4]:


# d
def BinarySearch(List, low, high, value):
    if low > high:
        return -1
    mid = (low + high) // 2
    if value > List[mid]:
        return BinarySearch(List, mid+1, high, value)
    elif value < List[mid]:
        return BinarySearch(List, low, mid-1, value)
    else:
        return mid

    
data = [1,2,3,4,5,6,7,8,9]
low = 0
high = len(data) - 1
value = 8
print(BinarySearch(data, low, high, value))


# In[10]:


# e
def Partition(Arr, left, right):
    pivot = Arr[left]
    low = left + 1
    high = right
    while True:
        while low <= high and Arr[high] >= pivot:
            high -=1
        while low <= high and Arr[low] <= pivot:
            low +=1
        if low <= high:
            Arr[low], Arr[high] = Arr[high], Arr[low]
        else:
            break
    Arr[left], Arr[high] = Arr[high], Arr[left]
    return high

def QuickSort(Arr, left, right):
    if left >= right:
        return
    part = Partition(Arr, left, right)
    QuickSort(Arr, left, part-1)
    QuickSort(Arr, part+1, right)


# In[11]:


lst = [2,8,2,1,4,7,8,5,323,1,42,7943,2,35,6,7]
left = 0
right = len(lst)-1
QuickSort(lst, left, right)
print(lst)

