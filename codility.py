import sys

# BinaryGap - Find maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N
def binary_gap(N):
    binary = str(bin(N)[2:])
    subarray, maximum = 0, 0
    for digit in binary:
        if digit is '0':
            subarray += 1
        else:
            maximum = subarray if subarray > maximum else maximum
            subarray = 0
    return maximum

# CyclicRotation - Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place
def cyclic_rotation(A, K):
    B = []
    if K > len(A):
        K = K % len(A)
    if len(A) == 0:
        return A
    else:
        for trans in range(K, 0, -1):
            B.append(A[len(A) - trans])
        for original in range(0, len(A) - K):
            B.append(A[original])
        A=B
    return A

# OddOccurrencesInArray - The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired
def odd_occurrences_in_array(A):
    element = 0;
    for i in A:
        element ^= i
    return element

# PermMissingElem - The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing. Find it
def perm_missing_elem(A):
    A.sort()
    missing=0
    if len(A) is 0 or A[0] != 1:
        return 1
    elif len(A) > 1:
        for i in range(0, len(A)-1):
            if A[i+1]-A[i] is 2:
                missing = A[i]+1
    return A[len(A)-1]+1 if missing is 0 else missing 
    
if __name__ is "__main__":
    print(binary_gap(1025))
    print(cyclic_rotation([1,2,3,4,5,6,7,8], 10))
    print(odd_occurrences_in_array([9,3,9,3,9,7,9]))
    print(perm_missing_elem([1,3]))
