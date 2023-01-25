#!/usr/bin/python3
"""Define classes for a singly-linked list
contains methods about the creation and hendling of
SinglyLinkedList and Node objects
"""


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
        """sets the data of the new node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data into a node"""
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
        """Initialises the linked list"""
        self.head = None

    def __str__(self):
        """Define the print representation of a SinglyLinkedList"""
        my_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                my_str += str(node.data) + '\n'
                node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list"""
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)

        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
