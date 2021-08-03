#!/usr/bin/env python3

class StringOP:
    def __init__(self, data):
        self.data = data
        
    def StrLength(self):
        count = 0
        for i in self.data:
            count +=1
        return count
    
    def StrConcat(self, string1, string2):
        newStr = ''
        for i in string1+string2:
            newStr+=i
        return newStr

    def SubString(self, text, start, end):
        subStr = ''
        for i in range(start, end+1):
            subStr += text[i]
        return subStr
    
    def InsertStr(self, data, text, pos):
        newStr = ''
        for i in range(len(data)):
            if i == pos:
                newStr = self.StrConcat(newStr, text)
                continue
            newStr+=data[i]
        return newStr
            
    def DeleteStr(self, data, pos, length):
        newStr = ''
        for i in range(len(data)):
            if i >= pos and i < pos+length:
                continue
            newStr+=data[i]
        return newStr
    
    def Naive(self, data, pattern):
        for i in range(0, len(data)):
            if data[i:i+len(pattern)] == pattern:
                return i
        return -1


s = StringOP('Hello Pythonic')
print(s.StrLength())
print(s.StrConcat('Hello', ' World'))
print(s.SubString('Hello', 2, 4))
print(s.InsertStr('Hello Wassay', ' Abdul ', 5))
print(s.DeleteStr('Hello Abdul Wassay', 7, 4))
print(s.Naive('My name is Wassay.', 'na'))

