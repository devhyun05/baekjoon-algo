ipv6 = input()

ipv6_split = ipv6.split("::")

if "::" in ipv6:
    left = ipv6_split[0] if ipv6_split[0] else []
    right = ipv6_split[1] if ipv6_split[1] else []

    if len(left) == 0:
        left = []
        splited_right = right.split(":")

        for i in range(len(splited_right)):
            splited_right[i] = ((4 - len(splited_right[i])) * "0") + splited_right[i]
        for _ in range(8 - len(splited_right)):
            left.append("0000")

        arr_add = left + splited_right
        print(":".join(arr_add))

    elif len(right) == 0:
        right = []
        splited_left = left.split(":")

        for i in range(len(splited_left)):
            splited_left[i] = ((4 - len(splited_left[i])) * "0") + splited_left[i]
        for _ in range(8 - len(splited_left)):
            right.append("0000")

        arr_add = splited_left + right
        print(":".join(arr_add))

    else:
        mid = []
        splited_left = left.split(":")
        splited_right = right.split(":")
        count_left = len(splited_left)
        count_right = len(splited_right)

        for i in range(count_left):
            if len(splited_left[i]) < 4:
                splited_left[i] = ((4 - len(splited_left[i])) * "0") + splited_left[i]

        for i in range(count_right):
            if len(splited_right[i]) < 4:
                splited_right[i] = ((4 - len(splited_right[i])) * "0") + splited_right[i]

        for _ in range(8 - (count_left + count_right)):
            mid.append("0000")

        arr_add = splited_left + mid + splited_right
        final_str = ":".join(arr_add)

        print(final_str)

else:
    ipv6_split = ipv6.split(":")

    for i in range(len(ipv6_split)):
        if len(ipv6_split[i]) < 4:
            zeros = "0" * (4 - len(ipv6_split[i]))
            ipv6_split[i] = zeros + ipv6_split[i]

    print(":".join(ipv6_split))