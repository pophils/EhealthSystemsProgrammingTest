

def gcd(a, b):
        """
        Function recursively finds the Greatest common divisor of two integers
        using Euclidean algorithm
        :param a: first integer
        :param b: second integer
        """
        # base cases
        if a == 0:
            return b
        if b == 0:
            return a

        return gcd(b, a % b)


def _lcm(a, b):
        """
        Function finds the LCM of two integers
        :param a: first integer
        :param b: second integer
        """
        if a == 0:
            return 0
        if b == 0:
            return 0

        _gcd = gcd(a, b)

        return (a*b) // _gcd


def lcm(input_array):
        """
        Function provides implementation of the Least Common Multiple of one or more integers.
        LCM(A,B) can be calculated efficiently by the division of (A * B) and GCD(A,B)
        GCD (greatest common divisor) of two pairs of integers can be solved
        by applying Euclidean Algorithm.
        """
        # Edge cases
        if input_array is None:
            raise ValueError('input list must not be none')

        if not isinstance(input_array, list):
            raise TypeError('input list must be a list type')

        if len(input_array) == 0:
            return []
        if len(input_array) == 1:
            return input_array[0]
        if sum(input_array) == 0:
            return 0

        try:
            current_lcm = _lcm(input_array[0], input_array[1])
            next_index = 2

            while next_index < len(input_array) and current_lcm != 0:
                current_lcm = _lcm(current_lcm, input_array[next_index])
                next_index += 1

            return current_lcm
        except TypeError:  # Edge case
            raise TypeError('One of the list element is not an integer type.')


if __name__ == '__main__':
    print('LCM of [20, 120, 40] is %d' % lcm([20, 120, 40]))
