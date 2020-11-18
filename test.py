# Course: CS261 - Data Structures
# Student Name: Leonel Garay
# Assignment: CS 261: Assignment 4
# Description: Binary Search Tree


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Method adds new value to the tree, maintaining BST property.
        """
        node = TreeNode(value)  # Creates a new tree Node using the value.
        start_obj = self.root  # First pointer.
        end_obj = None  # Second pointer.
        """ Iterates through the list as long as the start pointer is not None. """
        while start_obj is not None:
            end_obj = start_obj
            if start_obj.value > value:  # If object is greater than value add it to the left.
                start_obj = start_obj.left
            else:  # Else add it to the right.
                start_obj = start_obj.right
        if end_obj is None:  # Sets the root.
            end_obj = node
            self.root = end_obj
        elif value < end_obj.value:  # If value is less then leaf node add to left.
            end_obj.left = node
        else:  # Else add to right.
            end_obj.right = node

    def contains(self, value: object) -> bool:
        """
        Returns True if the value parameter is in the BinaryTree or False if its not in the tree.
        """
        start_obj = self.root
        while start_obj is not None:
            if value == start_obj.value:  # If the value was found, return True.
                return True
            elif value < start_obj.value:  # If value is less than value add it to the left.
                start_obj = start_obj.left
            else:  # If value is greater than value add it to the right.
                start_obj = start_obj.right
        return False

    def get_first(self) -> object:
        """
        Returns the value stored at the root node. If the BinaryTree is empty, this method returns None.
        """
        if self.root is not None:  # If the Root is not equal to node, return it.
            return self.root.value
        else:  # Else return None as the BinaryTree is empty.
            return None

def remove(self, value: object) -> bool:
"""
Removes first node with value property matching value argument
"""
# iterate through tree in search of value
left_bool = False
node_found = False
parent = None
to_remove = self.root
while to_remove is not None and not node_found:
if value == to_remove.value:
node_found = True
elif value < to_remove.value:
parent = to_remove
to_remove = to_remove.left
left_bool = True
else:
parent = to_remove
to_remove = to_remove.right
left_bool = False

# handle case where value was not found in BST
if not node_found:
return False

# handle case where node to remove is root
if to_remove == self.root:
self.remove_first()
return True

# handle case where to_remove is a leaf
if self.is_leaf(to_remove) and left_bool:
parent.left = None
return True
if self.is_leaf(to_remove) and not left_bool:
parent.right = None
return True

# handle case where to_remove only has left subtree
if to_remove.right is None and left_bool:
parent.left = to_remove.left
return True
if to_remove.right is None and not left_bool:
parent.right = to_remove.left
return True

# handle case where to_remove has a right subtree
# find left-most child from right subtree
left_bool_2 = False
replace_node = to_remove.right
replace_parent = to_remove
while replace_node.left is not None:
replace_parent = replace_node
replace_node = replace_node.left
left_bool_2 = True

# fill open slot from removing new_to_remove
if left_bool_2:
replace_parent.left = replace_node.right
if not left_bool_2:
replace_parent.right = replace_node.right

# insert left-most child from right subtree in open spot
if left_bool:
parent.left = replace_node
replace_node.left = to_remove.left
replace_node.right = to_remove.right
return True
if not left_bool:
parent.right = replace_node
replace_node.left = to_remove.left
replace_node.right = to_remove.right
return True