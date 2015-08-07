

def rotate(input_array, n=0):
    """
    Function rotate an integer array by a specified N position
    Rotation is done to avoid shifting elements which may lead to
    poor performance in case of a large sized array.
    :param input_array: array to be rotated
    :param n: N position(s)
    :return: rotated array
    """

    # Edge cases
    if input_array is None:
        raise ValueError('input list must not be none')

    if not isinstance(input_array, list):
        raise TypeError('input list must be a list type')

    if not isinstance(n, int):
        raise TypeError('N must be an integer type')

    if len(input_array) < 2:
        return input_array

    if n < 1:
        return input_array

    for i in range(n):
        input_array = input_array[-1:] + input_array[:-1]

    return input_array


if __name__ == '__main__':
    print('Rotation of [20, 120, 40] by 2 is %s' % rotate([20, 120, 40], 2))
