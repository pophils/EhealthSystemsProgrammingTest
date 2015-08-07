

import unittest
from Array_Rotation.array_rotation import rotate


class ArrayRotationTestCase(unittest.TestCase):

    def test_rotate_raises_value_error_on_undefined_input_array(self):
        with self.assertRaises(ValueError):
            rotate(None)

    def test_rotate_raises_type_error_on_a_non_list_type(self):
        with self.assertRaises(TypeError):
            rotate({})

    def test_rotate_raises_type_error_on_invalid_positioning(self):
        with self.assertRaises(TypeError):
            rotate([1, 2, 3, 4], 'invalid n')

    def test_rotate_returns_empty_array_if_input_array_is_empty(self):
        self.assertEqual(rotate([], n=2), [])

    def test_rotate_returns_same_array_if_input_array_has_one_element(self):
        self.assertEqual(rotate([20], n=2), [20])

    def test_rotate_returns_same_array_if_n_is_less_than_one(self):
        self.assertEqual(rotate([20, 23, 101], n=-2), [20, 23, 101])

    def test_rotate_returns_correct_output_on_valid_n(self):
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6], n=2), [5, 6, 1, 2, 3, 4])
        self.assertEqual(rotate([10, 25, 3, 11, 5, 16], n=3), [11, 5, 16, 10, 25, 3])

if __name__ == '__main__':
    unittest.main()
