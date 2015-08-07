

def compact(input_array):
    """
    Function compacts an sorted integer array by removing duplicates in the array.
    Doing this naively by creating another list to hold filtered elements will pose a
    problem in performance and might leads to program crash if array is substantially
    large. Space complexity will be quadratic i.e O(n**2)

    A better approach is to do the filtering in place without creating a new list or array.
    With this approach, complexity in terms of space and time will be linear i.e O(n)

    An automatic way of removing duplicate is to cast the array into a set (since it is an hash table-like
    ADT with unique keys without values) and consequently back to a list.

    :param input_array:
    :return: compacted array
    """

    # Edge cases
    if input_array is None:
        raise ValueError('input list must not be none')

    if not isinstance(input_array, list):
        raise TypeError('input list must be a list type')

    if len(input_array) < 2:
        return input_array

    next_index = 1
    previous_index = 0

    while next_index < len(input_array):
        if input_array[next_index] == input_array[previous_index]:
            input_array[previous_index + 1] = None
        else:
            input_array[previous_index + 1] = input_array[next_index]
            previous_index += 1

        next_index += 1
    del input_array[previous_index + 1:]

    return input_array


if __name__ == '__main__':
    print('Compaction of [1, 1, 3, 4, 4, 5, 6] gives %s' % compact([1, 1, 3, 4, 4, 5, 6]))