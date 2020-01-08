
def inversion_count(input_list: list) -> (list, int):
    """ Recursive inversion count with merge sort

    Complexity: O(n * log n)

    Examples:
        >>> inversion_count([1, 3, 5, 2, 4, 6])
        ([1, 2, 3, 4, 5, 6], 3)
        >>> inversion_count([1, 5, 0, 12, 17, 10])
        ([0, 1, 5, 10, 12, 17], 4)
        >>> inversion_count([2, 1])
        ([1, 2], 1)
    """

    if len(input_list) <= 1:
        return input_list, 0

    right_list_sorted, right_inversions = inversion_count(input_list[:len(input_list)//2])
    left_list_sorted, left_inversions = inversion_count(input_list[len(input_list)//2:])

    right_list_cursor, left_list_cursor, input_list_cursor = 0, 0, 0
    split_inversions = 0

    while right_list_cursor < len(right_list_sorted) and left_list_cursor < len(left_list_sorted):
        if right_list_sorted[right_list_cursor] < left_list_sorted[left_list_cursor]:
            input_list[input_list_cursor] = right_list_sorted[right_list_cursor]
            right_list_cursor += 1
        else:
            input_list[input_list_cursor] = left_list_sorted[left_list_cursor]
            left_list_cursor += 1
            split_inversions += len(right_list_sorted[right_list_cursor:])
        input_list_cursor += 1

    while right_list_cursor < len(right_list_sorted):
        input_list[input_list_cursor] = right_list_sorted[right_list_cursor]
        right_list_cursor += 1
        input_list_cursor += 1

    while left_list_cursor < len(left_list_sorted):
        input_list[input_list_cursor] = left_list_sorted[left_list_cursor]
        left_list_cursor += 1
        input_list_cursor += 1

    return input_list, right_inversions + left_inversions + split_inversions
