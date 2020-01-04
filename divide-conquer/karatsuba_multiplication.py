def karatsuba_multiplication(first_number: int, second_number: int) -> int:
    """Multiply two integers using recursive Karatsuba's algorithm

    Complexity: O (n ^ l o g 3)

    Examples:
        >>> karatsuba_multiplication(100, 120)
        12000
        >>> karatsuba_multiplication(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)
        8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    """

    first_number_len = len(str(first_number))
    second_number_len = len(str(second_number))

    # base case
    if first_number_len == 1 or second_number_len == 1:
        return first_number * second_number

    half_max_len = max(first_number_len, second_number_len) // 2

    a = first_number // (10 ** half_max_len)
    b = first_number % (10 ** half_max_len)

    c = second_number // (10 ** half_max_len)
    d = second_number % (10 ** half_max_len)

    z0 = karatsuba_multiplication(b, d)
    z1 = karatsuba_multiplication((a + b), (c + d))
    z2 = karatsuba_multiplication(a, c)

    return z2 * 10 ** (2 * half_max_len) + ((z1 - z2 - z0) * 10 ** half_max_len) + z0

