import sys 
from collections import deque 

input = sys.stdin.readline 

n = int(input())
dq = deque([])

for _ in range(n): 
    command = input().split()
    operation = command[0]
    
    if operation == "push_front":         
        dq.appendleft(command[1])
    elif operation == "push_back":
        dq.append(command[1])
    elif operation == "pop_front": 
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif operation == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif operation == "size":
        print(len(dq))
    elif operation == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif operation == "front": 
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif operation == "back":
        if dq: 
            print(dq[-1])
        else:
            print(-1)
    else:
        print("Operation not valid!")
    