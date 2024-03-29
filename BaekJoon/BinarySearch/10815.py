N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

for i in range(len(M_list)):
    left = 0
    right = len(N_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if N_list[mid] > M_list[i]:
            right = mid - 1
        elif N_list[mid] < M_list[i]:
            left = mid + 1
        elif N_list[mid] == M_list[i]:
            print(1, end=" ")
            break

    if left > right:
        print(0, end=" ")

# 이분 탐색 / remove 사용 X -> 해결
