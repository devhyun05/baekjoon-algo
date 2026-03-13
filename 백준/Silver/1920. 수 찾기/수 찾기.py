first_input = int(input())
first_numbers = list(map(int, input().split()))
num_map = {}

for i in range(len(first_numbers)):
    num_map[first_numbers[i]] = i 

second_input = int(input())
second_numbers = list(map(int, input().split()))

for num in second_numbers:
    if num in num_map:
        print(1)
    else:
        print(0)
