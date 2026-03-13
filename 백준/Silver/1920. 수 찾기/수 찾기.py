first_input = int(input())
first_numbers = list(map(int, input().split()))
num_set = set()

for num in first_numbers: 
    num_set.add(num)

second_input = int(input())
second_numbers = list(map(int, input().split()))

for num in second_numbers:
    if num in num_set: 
        print(1)
    else:
        print(0)