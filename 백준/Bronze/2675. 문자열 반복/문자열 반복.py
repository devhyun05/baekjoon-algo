import sys 
input = sys.stdin.readline 

n = int(input())

for _ in range(n):
    repeated_times, s = input().split()
    new_s = ""
    
    for c in s: 
        new_s += c * int(repeated_times)
       
    print(new_s)