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
            node = self.head
            while node:
                my_str += str(node.data)
                my_str += '\n'
                node = node.next_node
                return my_str[:-1]

        def sorted_insert(self, value):
            """Inserts a node in a sorted linked list"""
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
                return

            if value < self.head.data:
                new_node.next_node = self.head
                self.head = new_node
                return

            node = self.head
            while node.next_node and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
