

import unittest
from LCM.lcm import lcm, gcd, _lcm


class LCMTestCase(unittest.TestCase):

    def test_lcm_raises_value_error_on_undefined_input_array(self):
        with self.assertRaises(ValueError):
            lcm(None)

    def test_lcm_raises_type_error_on_a_non_list_type(self):
        with self.assertRaises(TypeError):
            lcm({})

    def test_gcd_of_two_integers_returns_the_other_integer_if_one_of_the_integer_is_zero(self):
        self.assertTrue(gcd(0, 1) == 1)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_of_two_integers_returns_the_right_output(self):
        self.assertTrue(gcd(10, 20) == 10)
        self.assertTrue(gcd(12, 20) == 4)
        self.assertTrue(gcd(5, 7) == 1)
        self.assertTrue(gcd(36, 100) == 4)

    def test_lcm_of_two_integers_returns_zero_if_at_least_one_integer_is_zero(self):
        self.assertTrue(_lcm(0, 1) == 0)
        self.assertEqual(_lcm(0, 0), 0)

    def test_lcm_of_two_integers_returns_the_right_output(self):
        self.assertTrue(_lcm(11, 4) == 44)
        self.assertTrue(_lcm(4, 11) == 44)
        self.assertTrue(_lcm(5, 2) == 10)
        self.assertTrue(_lcm(2, 5) == 10)
        self.assertTrue(_lcm(5, 202) == 1010)
        self.assertTrue(_lcm(202, 5) == 1010)

    def test_lcm_returns_an_empty_array_if_input_array_is_empty(self):
        self.assertEqual(lcm([]), [])

    def test_lcm_returns_first_integer_on_a_single_element_input_array(self):
        self.assertEqual(lcm([100]), 100)

    def test_lcm_returns_zero_if_all_the_input_array_elements_is_zero(self):
        self.assertEqual(lcm([0, 0, 0, 0, 0, 0]), 0)

    def test_lcm_compute_returns_correct_result_with_no_edge_case(self):
        self.assertEqual(lcm([10, 5]), 10)

        self.assertEqual(lcm([1, 0]), 0)

        self.assertEqual(lcm([2, 4, 16]), 16)

        self.assertEqual(lcm([2, 4, 16, 549]), 8784)

        self.assertEqual(lcm([202, 0, 567]), 0)

    def test_lcm_function_raises_type_error_if_input_array_contains_non_integer_element(self):
        with self.assertRaises(TypeError):
            self.assertEqual(lcm([2, 4, 16, 549, 'invalid input']), 8784)


if __name__ == '__main__':
    unittest.main()
