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

    def remove(self, value) -> bool:
        """
        Remove the first instance of the object in the BinaryTree.
        Returns True if the value is removed from the BinaryTree, otherwise returns False.
        """
        the_parent = None  # Set parent_node to None.
        the_victim = self.root  # Sets remove_node to root (used to find actual node)
        first_indicator = False  # Left is True, Right is False.
        second_indicator = False  # Sets second_indicator node.
        in_list_value = False  # Determines whether the value is on the BinaryTree or not.
        while the_victim is not None and in_list_value is False:  # Iterates through the tree to find the value.
            if value == the_victim.value:  # If the value is found set is_node to True.
                in_list_value = True
            elif value < the_victim.value:  # If the value is less than the root.
                the_parent = the_victim
                the_victim = the_victim.left
                first_indicator = True
            else:  # If the value is greater than the root.
                the_parent = the_victim
                the_victim = the_victim.right
                first_indicator = False
        if in_list_value is False:  # If the value is not on BinaryTree return False.
            return False
        if the_victim == self.root:  # If the value is a root.
            self.remove_first()
            return True
        if the_victim.left is None and the_victim.right is None and first_indicator is True:  # If the value is a leaf.
            the_parent.left = None
            return True
        if the_victim.left is None and the_victim.right is None and first_indicator is False:  # If the value is a leaf.
            the_parent.right = None
            return True
        if the_victim.right is None and first_indicator:  # Removing from when only a left.
            the_parent.left = the_victim.left
            return True
        if the_victim.right is None and first_indicator is False:
            the_parent.right = the_victim.left
            return True
        replace_node = the_victim.right
        replace_parent = the_victim
        while replace_node.left is not None:  # Removing from when right subtree.
            replace_parent = replace_node
            replace_node = replace_node.left
            second_indicator = True
        if second_indicator is True:
            replace_parent.left = replace_node.right
        if second_indicator is False:
            replace_parent.right = replace_node.right
        if first_indicator is True:
            the_parent.left = replace_node
            replace_node.left = the_victim.left
            replace_node.right = the_victim.right
            return True
        if first_indicator is False:
            the_parent.right = replace_node
            replace_node.left = the_victim.left
            replace_node.right = the_victim.right
            return True

    def remove_first(self) -> bool:
        """
        Remove the first instance of the object in the BinaryTree.
        Returns True if the value is removed from the BinaryTree, otherwise returns False.
        """
        if self.root is None:  # If BinaryTree is empty, return False.
            return False
        if TreeNode(self).left is None and TreeNode(self) is None:  # If root is leaf, set to None and return True.
            self.root = None
            return True
        if self.root.right is None:  # When there's only left subtree, replace and return True.
            self.root = self.root.left
            return True
        node_removed = self.root.right
        parent_removed = self.root
        left_node = False
        while node_removed.left is not None:  # When there is a right subtree.
            parent_removed = node_removed  # Sets the parent to the node to be removed.
            node_removed = node_removed.left  # Sets the node to be removed to whatever is on the left.
            left_node = True  # Sets left_node to True
        if left_node is True:  # If left_node is False, replace right of the parent to right of removed node.
            parent_removed.left = node_removed.right
        else:
            parent_removed.right = node_removed.right
        node_removed.left = self.root.left
        node_removed.right = self.root.right
        self.root = node_removed
        return True

    def pre_order_traversal_helper(self, node, new_queue):
        """
        Helper function for pre_order_traversal.
        """
        new_queue.enqueue(node)
        if node.left is not None:  # Navigates through the left.
            self.pre_order_traversal_helper(node.left, new_queue)
        if node.right is not None:  # Navigates through the right.
            self.pre_order_traversal_helper(node.right, new_queue)

    def pre_order_traversal(self):
        """
        Performs Pre-Order traversal of the tree and returns queue that contains the values of the visited node.
        """
        new_queue = Queue()
        if self.root is None:  # If tree is empty return new queue.
            return new_queue
        self.pre_order_traversal_helper(self.root, new_queue)
        return new_queue

    def in_order_traversal(self) -> Queue:
        """
        Performs In-Order traversal of the tree and returns queue that contains the values of the visited node.
        """
        new_queue = Queue()
        if self.root is None:  # If tree is empty return new queue.
            return new_queue
        self.in_order_traversal_helper(self.root, new_queue)
        return new_queue

    def in_order_traversal_helper(self, node, new_queue):
        """
        Helper function for in_order_traversal.
        """
        if node.left is not None:  # If there's a left side.
            self.in_order_traversal_helper(node.left, new_queue)
        new_queue.enqueue(node)   # Root.
        if node.right is not None:  # If there's a right side.
            self.in_order_traversal_helper(node.right, new_queue)

    def post_order_traversal(self) -> Queue:
        """
        Performs Post-Order traversal of the tree and returns queue that contains the values of the visited node.
        """
        new_queue = Queue()
        if self.root is None:  # If tree is empty return new queue.
            return new_queue
        self.post_order_traversal_helper(self.root, new_queue)
        return new_queue

    def post_order_traversal_helper(self, node, new_queue):
        """
        Helper function for post_order_traversal.
        """
        if node.left is not None:
            self.post_order_traversal_helper(node.left, new_queue)
        if node.right is not None:
            self.post_order_traversal_helper(node.right, new_queue)
        new_queue.enqueue(node)

    def by_level_traversal(self) -> Queue:
        """
        Performs By-Level traversal of the tree and returns queue that contains the values of the visited node.
        """
        new_queue = Queue()
        return new_queue

    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def height(self) -> int:
        """
        TODO: Write this implementation
        """
        return -1

    def count_leaves(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def count_unique(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())
