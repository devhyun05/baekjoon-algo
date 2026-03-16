def fast_pow(base, exp, modular):
    if exp == 0:
        return 1

    half = fast_pow(base, exp // 2, modular)

    if exp % 2 == 0:
        return (half * half) % modular
    else:
        return (half * half * base) % modular

nums = list(map(int, input().split()))
base = nums[0]
exp = nums[1]
modular = nums[2]

print(fast_pow(base, exp, modular))

