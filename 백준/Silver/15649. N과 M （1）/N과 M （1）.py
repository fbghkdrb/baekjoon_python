from itertools import permutations

N, M = map(int, input().split())
nums = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, permutations(nums, M)))))
