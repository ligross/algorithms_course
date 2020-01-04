
def merge_sort(input_list: list) -> list:
    """ Merge sort algorithm implementation

    Complexity: O(n * log n)

    Examples:
        >>> merge_sort([1, 5, 0, 12, 17, 10])
        [0, 1, 5, 10, 12, 17]
        >>> merge_sort([2, 1])
        [1, 2]
    """
    if len(input_list) <= 1:
        return input_list

    first_list = merge_sort(input_list[:len(input_list)//2])
    second_list = merge_sort(input_list[len(input_list)//2:])

    # merge two sorted lists

    first_list_cursor, second_list_cursor, input_list_cursor = 0, 0, 0

    for i in range(min(len(first_list), len(second_list))):
        if first_list[first_list_cursor] < second_list[second_list_cursor]:
            input_list[input_list_cursor] = first_list[first_list_cursor]
            first_list_cursor += 1
        else:
            input_list[input_list_cursor] = second_list[second_list_cursor]
            second_list_cursor += 1
        input_list_cursor += 1

    while first_list_cursor < len(first_list):
        input_list[input_list_cursor] = first_list[first_list_cursor]
        first_list_cursor += 1
        input_list_cursor += 1

    while second_list_cursor < len(second_list):
        input_list[input_list_cursor] = second_list[second_list_cursor]
        second_list_cursor += 1
        input_list_cursor += 1

    return input_list
