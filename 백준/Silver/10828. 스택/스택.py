# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n): 
    command = input().split()
    action = command[0]
    
    if action == "push":
        number = int(command[1]) 
        stack.append(number)
    elif action == "pop":
        if stack: 
            print(stack.pop())
        else:
            print(-1)
    elif action == "size":
        print(len(stack))
    elif action == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif action == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        print("Invalid input detected!")
      
        