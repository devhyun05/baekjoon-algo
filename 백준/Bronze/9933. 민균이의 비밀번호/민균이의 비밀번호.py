n = int(input())

text_map = {}

for _ in range(n):
    pwd = input()
    if pwd == pwd[::-1] or pwd in text_map:
        print(f"{len(pwd)} {pwd[len(pwd) // 2]}")
    else: 
        text_map[pwd[::-1]] = 0
       