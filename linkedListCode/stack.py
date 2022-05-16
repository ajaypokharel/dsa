'''
CSC 211
Spring 2022

A very basic implementation of a class for stacks
'''
from node import *

#--------------------------------------------------------------------------
class Stack():

    def __init__(self):
        self.size=0
        self.head=TwoWayNode()
        self.head.previous = self.head.next = self.head

    def push(self,key):
        ''' push key onto the top of the stack '''
        newNode=TwoWayNode(key, self.head, self.head.next)
        self.head.next=newNode
        newNode.next.previous=newNode
        self.size+=1

    def pop(self):
        ''' remove and return the top element from the stack '''
        # missing code goes here

    def peek(self):
        ''' return the value of the top element from the stack '''
        # missing code goes here

    def clear(self):
        '''clear the stack '''
        # missing code goes here

    def getSize(self):
        return self.size
     
    def printStack(self):
        ''' print all list elements in order '''
        nodeObject=self.head.next
        while nodeObject.data != None:
            print(nodeObject.data)
            nodeObject=nodeObject.next
        if(self.size==0):
            print("empty stack")

#--------------------------------------------------------------------------
#0 complete the methods for pop, peek, and clear
            
#1 define a new Stack object, push in several values, and print it out

s = Stack()

s.printStack()

s.push(23)
s.push(55)
s.push(12)

s.printStack()


#2 print the stack size, push in a few more values, and print the size again

#3 test pop and peek methods, make sure they work correctly

#4 clear the stack, print the stack and its size to confirm that it's empty

