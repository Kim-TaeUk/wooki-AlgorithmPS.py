import sys

N, K = map(int, sys.stdin.readline().split())
bag = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= bag[i - 1][0]:
            dp[i][j] = max(bag[i - 1][1] + dp[i - 1][j - bag[i - 1][0]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
