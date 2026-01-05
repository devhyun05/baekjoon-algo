from collections import deque

n = int(input())
dq = deque([i+1 for i in range(n)])

while len(dq) > 1:
    dq.popleft()
    num = dq.popleft()
    dq.append(num)

print(dq[0])