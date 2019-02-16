# Find the element that appears once

Given an array where every element occurs three times, except one element which occurs only once.
Find the element that occurs once.

## Example:
 Input: array[] = {1, 2, 3, 2, 3, 2, 10, 1, 1, 3}
 Output: 2

In the given array all element appear three times except 10 which appears just once.

# Solution approach:
The idea is to use bitwise operators for a solution that is O(n) time and uses O(1) extra space.
Run a loop for all elemts in arrat. At the end of every iteration, maintain following two values.
ones: The bits that have appeared 1st time or 4th time or 7th time,etc
twos: The bits that have appeared 2nd time, 5th time and 8th time, etc
Finally, we return the values of 'ones'.
### How to maintain the values of 'ones' and 'twos'?
'ones' and 'twos' are initialized as 0. For every new element in array, find out the common set bits in the new element and previous values of 'ones'.These common set bits are actually the bits that should be added to 'twos'. So do bitwise OR of the common set bits with 'twos'. 'twos' also get some extra bits that appear third time. These extra bits are removed later. Update 'ones' by doing XOR of new element with previous value of 'ones'. There may be some bits which appear 3rd time. These extra bits are also removed later.
Both 'ones' and 'twos' contain those extra bits which appear 3rd time. Remove these extra bits by finging out common set bits in 'ones' and 'twos'.