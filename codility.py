import sys

# BinaryGap - Find maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N
def solution(N):
    binary = str(bin(N)[2:])
    subarray, maximum = 0, 0
    for digit in binary:
        if digit is '0':
            subarray += 1
        else:
            maximum = subarray if subarray > maximum else maximum
            subarray = 0
    return maximum

if __name__ is "__main__":
    print(solution(1023))