#----------------------------------------------
#  CSC 211 - class examples with linked lists
#----------------------------------------------
from linkedlist import *


# create a new LinkedList object and put some values in it for testing
data=LinkedList()

data.append(49)
data.append(11)
data.append(56)
data.append(81)
data.append(62)
data.append(25)
data.append(74)
data.append(99)
data.append(30)
data.append(80)


# Methods to work on today

print("\n printList: ")
data.printList()

print("\n printListReversed: ")
data.printListReverse()

print("\n findListMax: ",data.findListMax())

print("\n findListMin: ",data.findListMin())

print("\n removeListMax: ")
data.removeListMax()
data.printList()

print("\n removeListMin: ")
data.removeListMin()
data.printList()




