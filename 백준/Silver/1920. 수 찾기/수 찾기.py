first_input = int(input())
first_numbers = list(map(int, input().split()))
first_numbers.sort()

second_input = int(input())
second_numbers = list(map(int, input().split()))

for num in second_numbers:
    start = 0
    end = len(first_numbers) - 1
    found_num = False

    while start <= end:
        mid = (start + end) // 2

        if first_numbers[mid] == num:
            found_num = True
            break
        elif first_numbers[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    if found_num:
        print(1)
    else:
        print(0)