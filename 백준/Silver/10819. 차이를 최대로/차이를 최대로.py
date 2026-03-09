def permute(nums):  
    res = []
    remaining = nums[:]
    def backtrack(curr_list, remaining):
        if len(curr_list) == len(nums):
            res.append(curr_list[:])
            return
        
        for i in range(len(remaining)): 
            curr_list.append(remaining[i])

            backtrack(curr_list, remaining[:i] + remaining[i+1:])
            curr_list.pop()

    backtrack([], remaining)
    return res 
    
how_many = int(input())
numbers = list(map(int, input().split()))
num_permute = permute(numbers)
n = len(num_permute)

sum_max = 0

for i in range(n): 
    m = len(num_permute[i])
    temp_sum = 0
    for j in range(m-1):

        curr_abs = abs(num_permute[i][j] - num_permute[i][j+1])
        temp_sum += curr_abs

    if temp_sum > sum_max: 
        sum_max = temp_sum 
        
print(sum_max)