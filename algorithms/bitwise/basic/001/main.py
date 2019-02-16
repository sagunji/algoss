def getSingle(arr, n):
    ones = 0
    twos = 0
    for i in range(n):
        # ones  & arr[i] gives the bits that are there in
        # both 'ones' and new element from arr[]
        # we add these bits to 'twos' using bitwise OR
        # Value of twos will be set as 0, 3, 4 and 1 after
        # 1st, 2nd, 3rd and 4th iteration respectively
        twos = twos | (ones & arr[i])

        # XOR the new bits with previous 'ones' to get all bits
        # appearing odd number of times
        # Values of 'ones' will be set as 3, 0, 2 and 3 after 1st,
        # 2nd, 3rd and 4th iteration respectively
        ones = ones ^ arr[i]
        # The common bits are those bits which appear third time.
        # So therse bits should be there in both 'ones' and 'twos'
        # common_bit_mask contans all these bits as 0, so that the bits can be
        # removed from 'ones' and 'twos'. Values of 'common_bit_mask' will be set
        # as 00, 00, 01 and 10 after 1st, 2nd, 3rd and 4th iterations respectively
        common_bit_mask = ~(ones & twos)
        # Remove common bits (the bits that appear third time)
        # from 'ones'. Valye of 'ones' will be set as 3, 0, 0
        # 2 after 1st, 2nd, 3rd and 4th iteration respectively
        ones &= common_bit_mask
        # Remove common bits (the bits that appear third time)
        # from 'twos'. Valyue of 'ones' will be set as 0, 3, 1
        # 2 after 1st, 2nd, 3rd and 4th iteration respectively
        twos &= common_bit_mask
    return ones


arr = [3, 3, 2, 3]
n = len(arr)
print(getSingle(arr, n))
