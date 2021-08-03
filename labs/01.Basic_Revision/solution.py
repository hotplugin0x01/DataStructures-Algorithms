#!/usr/bin/env python
# coding: utf-8

# Question 01
def EvenList(n):
    even_lst = []
    for count in range(n):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            even_lst.append(num)
    return even_lst

evenList = EvenList(6)
print(evenList)


# Question 02
def Max(List):
    return sorted(List)[-1]

lst = [1,2,3,5,6,8,9,43,21,4,-1,-0,-25]
out = Max(lst)
print(out)


# Question 03
def Min(List):
    return sorted(List)[0]

lst = [1,2,3,5,6,8,9,43,21,4,-1,-0,-25]
out = Min(lst)
print(out)


# Question 04
def Last(List):
    return List[-1]

lst = [13,6,7,9,0,8]
out = Last(lst)
print(out)


# Question 05
def KElement(List,k):
    if not k > len(List)-1:
        return List[k]

num_lst = [1,2,3,4,5]
k = 4
out = KElement(num_lst, k)
print(out)


# Question 06
def SecondLast(List):
    return List[-2]

lst = [9,4,6,7,9]
out = SecondLast(lst)
print(out)


# Question 07
def Reverse(List):
    return List[::-1]

lst = [1,2,3,4,6]
out = Reverse(lst)
print(out)


# Question 08
def Unique(List):
    unique_lst = []
    for num in List:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst

lst = [2,2,7,8,9,4,4,4,2,1,3]
out = Unique(lst)
print(out)


# Question 09
def UserNumbers():
    even_lst = []
    for i in range(10):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            even_lst.append(num)
    return even_lst[-1], max(even_lst), min(even_lst), even_lst[-2]
    
Last, Max, Min, secondLast = UserNumbers()
print(Last, Max, Min, secondLast, sep="\n")


# Question 10
def ShowExcitement():
    for i in range(5):
        print("A quick brown fox jumps over the lazy dog", end=" ")

ShowExcitement()


# Question 11
def Greater(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        return n1
    elif (n2 > n1) and (n2 > n3):
        return n2
    else:
        return n3
    
out = Greater(2, 9, 8)
print(out)


# Question 12
def divide(dividend, divisor):
    return dividend // divisor, dividend % divisor

quotient, remainder = divide(100, 50)
print(f"Quotient: {quotient}\nRemainder: {remainder}")


# Question 13
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def birthday(self):
        self.age += 1
        
p1 = Person("XYZ", 18)
print(p1.age)
p1.birthday()
print(p1.age)


# Home Task
import cmath

def PolarCoordinates(z):
    return cmath.polar(z)

z = 1+2j
r, faye = PolarCoordinates(z)
print(f"r= {r}\nfi= {faye}")