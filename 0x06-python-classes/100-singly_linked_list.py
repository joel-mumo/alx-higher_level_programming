#!/usr/bin/python3
"""Define classes for a singly-linked list"""


class Node:
    """This represents a node is a singly-linked list"""
    def __init__(self, data, next_node=None):
        """This initialises a new node
        Args:
            data (int): The value of the new Node.
            next_node (Node): The next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set the data of the new node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """set the next node of the current node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    class SinglyLinkedList:
        """Defines a singly-linked list"""
        def __init__(self):
            """Initialises a new singly-linked list"""
            self.__head = None

        def sorted_insert(self, value):
            """Insert a new Node to the SinglyLinkedList
            Args:
                value (Node): The new Node to insert.
            """
            new = Node(value)
            if self.__head is None:
                new.next_node = None
                self.__head = new
            elif self.__head.data > value:
                new.next_node = self.__head
                self.__head = new
            else:
                temp = self.__head
                while (temp.next_node is not None and
                        temp.next_node.data < value):
                    temp = temp.next_node
                    new.next_node = temp.next_node
                    temp.next_node = new

        def __str__(self):
            """Define the print behavior of a SinglyLinkedList"""
            values = []
            temp = self.__head
            while temp is not None:
                values.append(str(temp.data))
                temp = temp.next_node
            return ('\n'.join(values))
