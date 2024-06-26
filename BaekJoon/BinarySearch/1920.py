import sys

N = int(sys.stdin.readline().rstrip())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

for x in M_list:
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2

        if N_list[mid] > x:
            right = mid - 1
        elif N_list[mid] < x:
            left = mid + 1
        else:
            print(1)
            break
    if left > right:
        print(0)
