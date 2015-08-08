

import unittest
from Tree_Depth_First_Traversal.TreeADT import ArrayTree, TreeException


class ArrayTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = ArrayTree()

    def tearDown(self):
        if self.tree is not None:
            self.tree = None

    def test_root_returns_zero_index(self):
        self.tree = ArrayTree()
        self.tree.add_root([])

        self.assertEqual(self.tree.root(), 0)

    def test_root_raise_tree_exception_if_tree_is_empty(self):
        with self.assertRaises(TreeException):
            self.tree.root()

    def test_add_left_returns_correct_position(self):
        position = self.tree.add_root([])
        left_position_1 = self.tree.add_left(position, 'position 2')
        self.assertEqual(left_position_1, (position * 2) + 1)

        left_position_2 = self.tree.add_left(left_position_1, 'position 3')

        self.assertEqual(left_position_2, (left_position_1 * 2) + 1)

    def test_add_left_raises_tree_exception_if_a_left_already_exist(self):
        position = self.tree.add_root([])
        self.tree.add_left(position, 'position 2')

        with self.assertRaises(TreeException):
            self.tree.add_left(position, 'position 2')

    def test_add_right_returns_correct_position(self):
        position = self.tree.add_root([])
        right_position_1 = self.tree.add_right(position, 'position 2')
        self.assertEqual(right_position_1, (position * 2) + 2)

        right_position_2 = self.tree.add_right(right_position_1, 'position 3')

        self.assertEqual(right_position_2, (right_position_1 * 2) + 2)

    def test_add_right_raises_tree_exception_if_a_left_already_exist(self):
        position = self.tree.add_root([])
        self.tree.add_right(position, 'position 2')

        with self.assertRaises(TreeException):
            self.tree.add_right(position, 'position 2')

    def test_tree_pre_order(self):
        self.tree = ArrayTree()
        root_position = self.tree.add_root('root')

        l1 = self.tree.add_left(root_position, 'root left child')
        r1 = self.tree.add_right(root_position, 'root right child')

        self.tree.add_left(l1, 'A new left child')
        r2 = self.tree.add_right(r1, 'A new right child')

        self.tree.add_right(r2, 'right child 3')
        l3 = self.tree.add_left(r2, 'left child 3')

        r4 = self.tree.add_right(l3, 'right child 4')
        self.tree.add_left(l3, 'left child 4')

        self.tree.add_right(r4, 'right child 5')
        self.tree.add_left(r4, 'left child 5')

        pre_ordered_element = []
        for pos in self.tree.pre_order():
            pre_ordered_element.append(self.tree.element(pos))

        self.assertListEqual(['root', 'root left child',
                              'A new left child', 'root right child',
                              'A new right child', 'left child 3',
                              'left child 4', 'right child 4', 'left child 5',
                              'right child 5', 'right child 3'], pre_ordered_element)

    def test_tree_post_order(self):
        self.tree = ArrayTree()
        root_position = self.tree.add_root('root')

        l1 = self.tree.add_left(root_position, 'root left child')
        r1 = self.tree.add_right(root_position, 'root right child')

        self.tree.add_left(l1, 'A new left child')
        r2 = self.tree.add_right(r1, 'A new right child')

        self.tree.add_right(r2, 'right child 3')
        l3 = self.tree.add_left(r2, 'left child 3')

        r4 = self.tree.add_right(l3, 'right child 4')
        self.tree.add_left(l3, 'left child 4')

        self.tree.add_right(r4, 'right child 5')
        self.tree.add_left(r4, 'left child 5')

        post_ordered_element = []
        for pos in self.tree.post_order():
            post_ordered_element.append(self.tree.element(pos))

        self.assertListEqual(['A new left child', 'root left child',
                              'left child 4', 'left child 5', 'right child 5',
                              'right child 4', 'left child 3', 'right child 3',
                              'A new right child', 'root right child', 'root'], post_ordered_element)

    def test_tree_in_order(self):
        self.tree = ArrayTree()
        root_position = self.tree.add_root('root')

        l1 = self.tree.add_left(root_position, 'root left child')
        r1 = self.tree.add_right(root_position, 'root right child')

        self.tree.add_left(l1, 'A new left child')
        r2 = self.tree.add_right(r1, 'A new right child')

        self.tree.add_right(r2, 'right child 3')
        l3 = self.tree.add_left(r2, 'left child 3')

        r4 = self.tree.add_right(l3, 'right child 4')
        self.tree.add_left(l3, 'left child 4')

        self.tree.add_right(r4, 'right child 5')
        self.tree.add_left(r4, 'left child 5')

        in_ordered_element = []
        for pos in self.tree.in_order():
            in_ordered_element.append(self.tree.element(pos))

        self.assertListEqual(['A new left child', 'root left child',
                              'root', 'root right child', 'left child 4',
                              'left child 3', 'left child 5', 'right child 4',
                              'right child 5', 'A new right child', 'right child 3'], in_ordered_element)

if __name__ == '__main__':
    unittest.main()
