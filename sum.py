def even(limit):
    for n in range(2, limit + 1, 2):
        if 80 <= n <= 90:
            continue
        else:
            print(n)

def odd(limit):
    for n in range(1, limit + 1, 2):
        if 30 <= n <= 40:
            continue
        else:
            print(n)

limit = 100
even(limit)
odd(limit)
