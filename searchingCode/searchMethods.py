# -------------------------------------
# CSC 211 - searchMethods.py
# -------------------------------------
import matplotlib.pyplot as plt
from random import *
import time


# sequential search
def seqSearch(arr,key):
    i=0
    while i<len(arr):
        if(arr[i]==key):
            return i
        i+=1
    return -1

# binary search
def binarySearch(arr,key):
    left=-1
    right=len(arr)

    while left<right-1:
        mid=(left+right)//2
        # test for location of key 
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            left=mid        # key is in right half
        else:
            right=mid       # key is in left half
            
    return -1
  
# create a sorted list
n=20
data=[]
for x in range(n):
    data.append(randrange(n))

data.sort()
print(data)


# choose a key and test the search method
k=randrange(n)
print("key = ",k)
print("sequential search return = ",seqSearch(data,k))

print("binary search return = ",binarySearch(data,k))
