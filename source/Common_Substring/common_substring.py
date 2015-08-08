

def find_common_substring_quadratic(string_a, string_b):
    """
    Function find and return the common substring in the two input
    strings in the order they are found in the first string.

    This version naively find the substring in quadratic time complexity
    i.e O(n**2)
    :param string_a:First input string
    :param string_b:Second input string
    :return: The common substring
    """

    # Edge cases
    if string_a is None or string_b is None:
        raise ValueError('The two input string must not be none')

    if not isinstance(string_a, str):
        raise TypeError('string_a must be a str type')

    if not isinstance(string_b, str):
        raise TypeError('string_b must be a str type')

    string_a, string_b = string_a.strip().lower(), string_b.strip().lower()

    if len(string_a) == 0 or len(string_b) == 0:
        return ''

    common_substring = ''

    for i in range(len(string_a)):
        if string_a[i] != ' ':
            for j in range(len(string_b)):
                if string_b[j] == string_a[i]:
                    common_substring += string_a[i]
                    break

    return common_substring


def find_common_substring_linear(string_a, string_b):
    """
    Function find and return the common substring in the two input
    strings in the order they are found in the first string.

    This version efficiently find the substring in a linear time complexity
    i.e O(n) using an hash set.

    :param string_a:First input string
    :param string_b:Second input string
    :return: The common substring
    """

    # Edge cases
    if string_a is None or string_b is None:
        raise ValueError('The two input string must not be none')

    if not isinstance(string_a, str):
        raise TypeError('string_a must be a str type')

    if not isinstance(string_b, str):
        raise TypeError('string_b must be a str type')

    string_a, string_b = string_a.strip().lower(), string_b.strip().lower()

    if len(string_a) == 0 or len(string_b) == 0:
        return ''

    string_b_hash_set = set(string_b)  # O(n) linear complexity
    common_substring = ''

    for i in range(len(string_a)):  # O(n) linear complexity
        if string_a[i] != ' ':
            if string_a[i] in string_b_hash_set:  # constant time lookup
                common_substring += string_a[i]

    return common_substring
