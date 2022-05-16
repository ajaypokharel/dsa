# -------------------------------------
# CSC 211 - fastSortingMethods.py
# Note: needs arrays.py
# -------------------------------------
from random import *
import time
from arrays import Array

#----------------------------------------------------------
# Mergesort

# main function called by the user
def mergeSort(arr):
    n=len(arr)
    copyBuffer=Array(n)                     #
    mergeSortHelper(arr,copyBuffer,0,n-1)   #

# helper function that contains the recursive function calls
def mergeSortHelper(arr,copyBuffer,low,high):
    if low<high:
        middle=(low+high)//2
        #print('recursive call',low,' -- ',middle)
        mergeSortHelper(arr,copyBuffer,low,middle)      #
        #print('recursive call',middle+1,' -- ',high)
        mergeSortHelper(arr,copyBuffer,middle+1,high)   #
        #print('merge back together')
        merge(arr,copyBuffer,low,middle,high)           #

# function to merge two sorted subarrays back together
def merge(arr,copyBuffer,low,middle,high):
    i1=low
    i2=middle+1
    for i in range(low,high+1):     #
        if i1>middle:               #
            copyBuffer[i]=arr[i2]   
            i2+=1                   
        elif i2>high:               #
            copyBuffer[i]=arr[i1]
            i1+=1
        elif arr[i1]<arr[i2]:       #
            copyBuffer[i]=arr[i1]
            i1+=1
        elif arr[i1]>=arr[i2]:      #
            copyBuffer[i]=arr[i2]
            i2+=1
    for i in range(low,high+1):     #
        arr[i]=copyBuffer[i]
        
#----------------------------------------------------------
# Quicksort

# function to swap two values in a list/array
def swap(arr,i,j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def quickSort(arr):
    n=len(arr)
    return quickSortHelper(arr, 0, n-1)

def quickSortHelper(arr, left, right):
    count=0
    if left < right:
        count+=right-left
        pivotLocation = partition(arr, left, right)
        count+=quickSortHelper(arr, left, pivotLocation - 1)
        count+=quickSortHelper(arr, pivotLocation + 1, right)
    return count

def partition(arr, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = arr[middle]
    arr[middle] = arr[right]
    arr[right] = pivot
    
    # Set boundary point to first position
    boundary = left
    
    # Move items less than pivot to the left
    for index in range(left, right):
        if arr[index] < pivot:
            swap(arr, index, boundary)
            boundary += 1
            
    # Exchange the pivot item and the boundary item
    swap(arr, right, boundary)
    return boundary
        

#----------------------------------------------------------
# test the algorithms out

##n=800
##
##
##total=0
##for i in range(10000):
##    data=[]
##    for x in range(n):
##        data.append(randrange(10*n))
##
##    work=quickSort(data)
##    total+=work
##
##avg_work=total/10000
##
##print('average work = ',avg_work)

a=[4,2,0,7,3,5,8,1,6]

partition(a,0,8)

print(a)
    

