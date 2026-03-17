n = int(input())
num_list = []
num_map = {}

for i in range(n):
    num = int(input())
    num_list.append(num)

n = len(num_list)

for i in range(n):
    for j in range(n):
        comb = num_list[i] + num_list[j]
        num_map[comb] = 0

num_list.sort()
num_found = False 
for i in range(n-1, -1 ,-1):
    for j in range(i-1, -1, -1):

        comb = num_list[i] - num_list[j]
        if comb in num_map:
            print(num_list[i])
            num_found = True 
            break 
    if num_found:
        break 
        

    
    