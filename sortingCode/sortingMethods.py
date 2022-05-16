# -------------------------------------
# CSC 211 - sortingMethods.py
# Note: needs arrays.py
# -------------------------------------
#import matplotlib.pyplot as plt
from random import *
import time

# function to swap two values in a list/array
def swap(arr,i,j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp

# selection sort function
def selectionSort(arr):
    numComps=0
    numSwaps=0
    i=0
    while i<len(arr)-1:
        minIndex=i
        j=i+1
        while j<len(arr):
            numComps+=1
            if arr[j]<arr[minIndex]:
                minIndex=j
            j+=1
        if minIndex!=i:
            swap(arr,minIndex,i)
            numSwaps+=1
        i+=1
    return( numComps + 0*numSwaps )

# bubble sort function
def bubbleSort(arr):
    numComps=0
    numSwaps=0
    n=len(arr)
    while n>1:
        i=1
        while i<n:
            numComps+=1
            if arr[i]<arr[i-1]:
                swap(arr,i,i-1)
                numSwaps+=1
            i+=1
        n-=1
    return( numComps + 0*numSwaps )

# insertion sort function
def insertionSort(arr):
    numComps=0
    numSwaps=0
    i=1
    while i<len(arr):
        itemToInsert=arr[i]
        j=i-1
        numComps+=1
        while j>=0 and itemToInsert<arr[j]:
            numComps+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=itemToInsert
        numSwaps+=1
        i+=1
    return( numComps + 0*numSwaps )


#----------------------------------------------------------

n=400

# Already sorted 
data=[0]
for x in range(n):
    data.append(data[-1] + randrange(10))
 

# Completely Unsorted
#data=[]
#for x in range(n):
#    data.append(randrange(10*n))


# Reverse Sorted
#data=[10*n]
#for x in range(n):
#    data.append(data[-1] - randrange(10))

 
#print("\n initial: ",data)

work = selectionSort(data)
#work = bubbleSort(data)
#work = insertionSort(data)

#print("\n sorted:  ",data)

print("\n n = ",n)
print(" work = ",work)

