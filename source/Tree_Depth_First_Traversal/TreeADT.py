
class TreeException(Exception):
    pass


class ArrayTree(object):
    """
    Class provides an implementation of Depth first traversal of A tree.
    Class makes use of an array based binary tree.

    Depth first tree traversal unlike breadth-first is in three variant namely:
    Pre-order traversal where the parent node is processed before child nodes.
    Post-order traversal where child nodes are processed before the parent node
    In-order traversal where the left subtree of a node is processed followed by the node
    and finally its right subtree.

    A simple application is found when walking through a file directory.

    To demonstrate the traversal, the following steps can be done
    - Instantiate a new tree with or without the a default capacity,
    - Add the root element,
    - Add other nodes to the tree
    - Calling any of the traversal method recursively yields position index of each node.
    - Loop through the positions yielded and call element(position) to get the each values

    """

    def __init__(self, default_capacity=20):

        if default_capacity is not None and not isinstance(default_capacity, int):
            raise TypeError("The defaultCapacity must be an integer.")
        self.__default_capacity = default_capacity

        self.__data = [None] * self.__default_capacity
        self.__size = 0

    def root(self):
        if self.__data[0] is None:
            raise TreeException("The tree is empty.")
        return 0

    def add_root(self, e):
        if self.__data[0] is not None:
            raise TreeException("The tree already has a root.")

        self.__data[0] = e
        self.__size = 1

        return 0

    def add_left(self, i, e):

        self.__validate_level_number(i)

        if self.__has_left(i):
            raise TreeException("This position already has a left child.")

        new_position = (i*2) + 1

        if new_position > len(self.__data):
            self.__resize(2*len(self.__data))

        self.__data[new_position] = e

        self.__size += 1

        return new_position

    def add_right(self, i, e):

        self.__validate_level_number(i)

        if self.__has_right(i):
            raise TreeException("This position already has a right child.")

        new_position = (i*2) + 2

        if new_position > len(self.__data):
            self.__resize(2*len(self.__data))

        self.__data[new_position] = e

        self.__size += 1

        return new_position

    def num_of_children(self, i):
        """
        Returns the number of children of a node at index i
        :param i: position index
        """
        self.__validate_level_number(i)
        count = 0

        if self.__has_left(i):
            count = 1
        if self.__has_right(i):
            count += 1

        return count

    def element(self, i):
        """
        Returns the number of children of a node at index i
        :param i: position index
        """
        self.__validate_level_number(i)

        return self.__data[i]

    def left(self, i):
        self.__validate_level_number(i)

        if not self.__has_left(i):
            return None

        return (i*2) + 1

    def right(self, i):
        self.__validate_level_number(i)

        if not self.__has_right(i):
            return None

        return (i*2) + 2

    def parent(self, i):
        self.__validate_level_number(i)
        return (i - 1) // 2

    def is_root(self, i):
        """
        Returns True if position is the root of the tree.
        :param i: level number
        :return: Boolean
        """
        return i == 0

    def children(self, i):
        self.__validate_level_number(i)

        if self.__has_left(i):
            yield self.left(i)

        if self.__has_right(i):
            yield self.right(i)

    def is_empty(self):
        return self.__size == 0

    def pre_order(self):
        if self.is_empty():
            return None
        for position in self.__pre_order(self.root()):
            yield position

    def post_order(self):
        if self.is_empty():
            return None
        for position in self.__post_order(self.root()):
            yield position

    def in_order(self):
        if self.is_empty():
            return None
        for position in self.__in_order(self.root()):
            yield position

    def __post_order(self, i):
        for child in self.children(i):
            for pos in self.__post_order(child):
                yield pos
        yield i

    def __pre_order(self, i):
        yield i
        for child in self.children(i):
            for pos in self.__pre_order(child):
                yield pos

    def __in_order(self, i):

        left_child = self.left(i)
        right_child = self.right(i)

        if left_child is not None:
            for pos in self.__in_order(left_child):
                yield pos

        yield i

        if right_child is not None:
            for pos in self.__in_order(right_child):
                yield pos

    def __len__(self):
        return self.__size

    def __resize(self, new_len):

        temp_buffer = [None] * new_len

        for cursor in range(len(self.__data)):
            temp_buffer[cursor] = self.__data[cursor]

        self.__data = temp_buffer

    def __is_leaf(self, i):
        return self.num_of_children(i) == 0

    def __has_left(self, i):
        return (i * 2) + 1 < len(self.__data) and self.__data[(i * 2) + 1] is not None

    def __has_right(self, i):
        return (i * 2) + 2 < len(self.__data) and self.__data[(i * 2) + 2] is not None

    def __validate_level_number(self, i):
        if i >= len(self.__data):
            raise IndexError("Index is not a valid level number.")


if __name__ == '__main__':
    tree = ArrayTree()

    root_position = tree.add_root('root')

    l1 = tree.add_left(root_position, 'root left child')
    r1 = tree.add_right(root_position, 'root right child')

    l2 = tree.add_left(l1, 'A new left child')
    r2 = tree.add_right(r1, 'A new right child')

    r3 = tree.add_right(r2, 'right child 3')
    l3 = tree.add_left(r2, 'left child 3')

    r4 = tree.add_right(l3, 'right child 4')
    l4 = tree.add_left(l3, 'left child 4')

    r5 = tree.add_right(r4, 'right child 5')
    l5 = tree.add_left(r4, 'left child 5')

    print("All tree elements via Pre-order traversal")
    for pos in tree.pre_order():
        print("\t", tree.element(pos))

    print("All tree elements via Post-order traversal")
    for pos in tree.post_order():
        print("\t", tree.element(pos))

    print("All tree elements via In-order traversal")
    for pos in tree.in_order():
        print("\t", tree.element(pos))
