import sys

N = int(sys.stdin.readline().rstrip())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort()

for number in numbers:
    print(number)
