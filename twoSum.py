from itertools import combinations
from math import floor


def twoSum(arr, target):
    pairs = list(combinations(arr, 2))
    diff = []

    for pair in pairs:
        diff.append(round(round(pair[0] + pair[1], 1) - target, 1))

    diff = list(map(lambda x: abs(x), diff))

    smallestPair = diff[0]
    smallestPairIndex = 0
    for pair in diff:
        if smallestPair > pair:
            smallestPair = pair
            smallestPairIndex = diff.index(smallestPair)

    return pairs[smallestPairIndex]


print(twoSum([2, 3, 7, 11, 15], 23))
