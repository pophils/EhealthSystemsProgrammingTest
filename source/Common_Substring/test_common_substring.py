

import unittest
from Common_Substring.common_substring import find_common_substring_quadratic, find_common_substring_linear


class CommonSubstringTestCase(unittest.TestCase):

    def test_find_common_substring_raises_value_error_on_undefined_inputs(self):
        with self.assertRaises(ValueError):
            find_common_substring_quadratic(None, None)

        with self.assertRaises(ValueError):
            find_common_substring_linear(None, None)

    def test_find_common_substring_raises_type_error_on_a_non_string_type(self):
        with self.assertRaises(TypeError):
            find_common_substring_quadratic({}, 1234)

        with self.assertRaises(TypeError):
            find_common_substring_linear({}, 1234)

    def test_find_common_substring_returns_empty_string_if_first_string_is_empty(self):
        self.assertEqual(find_common_substring_quadratic('', 'string 2'), '')

        self.assertEqual(find_common_substring_linear('', 'string 2'), '')

    def test_find_common_substring_returns_correct_output_on_valid_input_strings(self):
        self.assertEqual(find_common_substring_quadratic('ABCDEF', 'ABCDEFGH'), 'ABCDEF')
        self.assertEqual(find_common_substring_quadratic('SABCDEF', 'FCZ3DRES'), 'SCDEF')
        self.assertEqual(find_common_substring_quadratic('techcrunch', 'the next web'), 'tehn')

        self.assertEqual(find_common_substring_linear('ABCDEF', 'ABCDEFGH'), 'ABCDEF')
        self.assertEqual(find_common_substring_linear('SABCDEF', 'FCZ3DRES'), 'SCDEF')
        self.assertEqual(find_common_substring_linear('techcrunch', 'the next web'), 'tehn')

if __name__ == '__main__':
    unittest.main()
