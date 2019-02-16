def getSingle(arr, n):
    ones = 0
    twos = 0
    for i in range(n):
        # ones  & arr[i] gives the bits that are there in
        # both 'ones' and new element from arr[]
        # we add these bits to 'twos' using bitwise OR
        twos = twos | (ones & arr[i])
        # XORing the 'ones' and the new elements such that new value is assigned to ones
        ones = ones ^ arr[i]
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones


arr = [3, 3, 3, 2]
n = len(arr)
print(getSingle(arr, n))
