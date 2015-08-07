

import unittest
from Array_Compaction.array_compaction import compact


class ArrayCompactionTestCase(unittest.TestCase):

    def test_compact_raises_value_error_on_undefined_input_array(self):
        with self.assertRaises(ValueError):
            compact(None)

    def test_compact_raises_type_error_on_a_non_list_type(self):
        with self.assertRaises(TypeError):
            compact({})

    def test_compact_returns_empty_array_if_input_array_is_empty(self):
        self.assertEqual(compact([]), [])

    def test_compact_returns_same_array_if_input_array_has_one_element(self):
        self.assertEqual(compact([20]), [20])

    def test_compact_returns_correct_output_on_valid_input_array(self):
        self.assertEqual(compact([1, 1, 3, 4, 4, 5, 6]), [1, 3, 4, 5, 6])
        self.assertEqual(compact([100, 71, 71, 71, 35, 16, 12, 9, 9, 0, 0]), [100, 71, 35, 16, 12, 9, 0])

if __name__ == '__main__':
    unittest.main()
