import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = input().split()
dq = deque([])
answer = []
next_pos = 0

for i in range(n):
    dq.append((i + 1, int(numbers[i])))

for i in range(n):
    if next_pos < 0:
        for _ in range(abs(next_pos)):
            dq.appendleft(dq.pop())
    else:
        for _ in range(next_pos - 1):
            dq.append(dq.popleft())

    target_ballon = dq.popleft()
    answer.append(target_ballon[0])
    next_pos = target_ballon[1]

print(" ".join(map(str, answer)))



