import sys
from collections import deque 

user_input = sys.stdin.readline().split()
n = int(user_input[0])
k = int(user_input[1])

dq = deque(range(1, n+1))
answer = []

while dq: 
    for _ in range(k-1): 
        dq.append(dq.popleft())
    answer.append(dq.popleft())

print("<" + ", ".join(map(str, answer)) + ">")
