import sys

N = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(100 + 1)]
dp[1] = 1
dp[2] = 1
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
