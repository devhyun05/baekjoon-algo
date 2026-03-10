plate = int(input())

def hanoi_tower(n, fr, mid, to):
    if n == 0:
        return
    
    hanoi_tower(n - 1, fr, to, mid)
    print(fr, to)
    hanoi_tower(n - 1, mid, fr, to)

print(2**plate - 1)

if plate <= 20:
    hanoi_tower(plate, 1, 2, 3)