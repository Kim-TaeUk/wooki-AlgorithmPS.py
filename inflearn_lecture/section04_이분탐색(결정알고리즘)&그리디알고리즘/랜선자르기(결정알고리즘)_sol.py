def count(len):
    cnt = 0
    for x in k_list:
        cnt += x // len

    return cnt


K, N = map(int, input().split())
k_list = []
for _ in range(K):
    k_list.append(int(input()))

res = 0
left = 1
right = max(k_list)

while left <= right:
    mid = (left + right) // 2
    if count(mid) >= N:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
# 결정 알고리즘 방법론에서 이분 검색을 사용함
# 답이 특정 범위 안에 있다라는 것을 알때 결정 알고리즘을 사용함
