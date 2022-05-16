#-------------------------------------------
# CSC 211 - examples with BSTs 
#-------------------------------------------

from linkedbst import *


print('\n TEST #1')

myTree=LinkedBST()

myTree.add(5)
myTree.add(3)
myTree.add(7)

print(myTree)

print('\n test the sum function:')
print('sum = ',myTree.sum())


print('\n test the count function:')
print('count = ',myTree.count())


print('\n TEST #2')

myTree=LinkedBST()

myTree.add(50)
myTree.add(81)
myTree.add(22)
myTree.add(43)
myTree.add(64)
myTree.add(75)
myTree.add(36)
myTree.add(97)

print(myTree)

print('\n test the sum function:')
print('sum = ',myTree.sum())


print('\n test the count function:')
print('count = ',myTree.count())


print('\n TEST #3')

myTree=LinkedBST()

myTree.add(22)
myTree.add(33)
myTree.add(44)
myTree.add(55)
myTree.add(66)

print(myTree)

print('\n test the sum function:')
print('sum = ',myTree.sum())


print('\n test the count function:')
print('count = ',myTree.count())
