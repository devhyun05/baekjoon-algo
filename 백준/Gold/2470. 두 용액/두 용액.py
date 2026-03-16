n = int(input())
nums = list(map(int, input().split()))
nums.sort()
p1 = 0
p2 = len(nums)-1 
closest_to_zero = float("inf")
ans1, ans2 = 0, 0

while p1 < p2: 
    num_sum = nums[p1] + nums[p2]
    
    if abs(num_sum) < closest_to_zero:
        ans1, ans2 = nums[p1], nums[p2]
        closest_to_zero = abs(num_sum)
    
    if num_sum < 0: 
        p1 += 1 
    else:
        p2 -= 1 

print(ans1, ans2)