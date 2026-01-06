import sys
from collections import deque 

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n): 
    command = sys.stdin.readline().split()
    action = command[0]
    
    if action == "push": 
        number = command[1]
        dq.append(number)
    elif action == "pop":
        if dq: 
            print(dq.popleft())
        else:
            print(-1)
    elif action == "size":
        print(len(dq))
    elif action == "empty":
        if dq: 
            print(0)
        else:
            print(1)
    elif action == "front":
        if dq: 
            print(dq[0])
        else:
            print(-1)
    elif action == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
    else:
        print("Invalid input")
        