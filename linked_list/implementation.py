from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = elements
        self.start = None
        self.end = None
        if self.elements:
            for e in range(0, len(elements)):
                self.elements[e] = Node(self.elements[e])
            for e in range(0, len(elements)-1):
                self.elements[e].next = self.elements[e+1]
            self.start = self.elements[0]
            self.end = Node(self.elements[-1])
        else:
            self.elements = []

    def __str__(self):
        return('{}'.format(self.elements))

    def __len__(self):
        return(len(self.elements))

    def __iter__(self):
        return self.start

    def __getitem__(self, index):
        return(self.elements[index])

    def __add__(self, other):
        if self.elements:
            if other.elements:
                addition = self.elements + other.elements
            else:
                addition = self.elements + []
        else:
            if other.elements:
                addition = [] + other.elements
            else:
                addition = self
        return(addition)

    def __iadd__(self, other):
        if self.elements:
            if other.elements:
                addition = self.elements + other.elements
            else:
                addition = self.elements + []
        else:
            if other.elements:
                addition = [] + other.elements
            else:
                addition = self
        return(addition)

    def __eq__(self, other):
        if self.elements != other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.elements != other:
            return True
        else:
            return False

    def append(self, elem):
        newNode = Node(elem)
        if self.end:
            self.end.next = newNode
            self.elements = self.elements + [newNode]
        else:
            if elem >= 1:
                self.start = newNode
                self.end = newNode
            self.elements = [newNode]
        return(self)

    def count(self):
        return len(self.elements)

    def pop(self, index=None):
        if index is not None:
            number = self.elements.pop(index)
            return(number)
        else:
            number = self.elements.pop()
            return(number)


