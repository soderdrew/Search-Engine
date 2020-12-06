"""This is Lab 3 where we cover stack ADT in
an array and singly-linked-list
Course: CPE 202
Quarter: Spring 2020
Author: Drew Soderquist"""


class Node:
    """An Int List is one of
        -None, or
        -Node(val, next, prev): An Int List
    Attributes:
        val(int): the payload
        nxt(Node): the next item in the list
    """
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return f"Node({self.val}, {self.nxt})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.val == other.val and self.nxt == other.nxt

    def get_val(self):
        """gets value of a node
        Attributes:
            N/A
        Returns:
            int: value of the node
        """
        return self.val

    def get_next(self):
        """gets next node
        Attributes:
            N/A
        Returns:
            node: next node
        """
        return self.nxt

    def set_val(self, newval):
        """sets value of a node
        Attributes:
            N/A
        Returns:
            int: new value of the node
        """
        self.val = newval

    def set_next(self, newnext):
        """sets next node
        Attributes:
            N/A
        Returns:
            Node: new next node"""
        self.nxt = newnext
