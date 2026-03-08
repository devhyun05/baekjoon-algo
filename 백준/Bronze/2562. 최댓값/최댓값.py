import sys 

nums = [int(sys.stdin.readline()) for _ in range(9)]
max_num = -1 
max_num_index = -1 
n = len(nums)

for i in range(n): 
    if nums[i] > max_num: 
        max_num = nums[i]
        max_num_index = i+1 

print(max_num)
print(max_num_index)