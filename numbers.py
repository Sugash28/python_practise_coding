def number(n):
    last = n % 10
    first = n
    while first >= 10:
        first //= 10
    print("First digit:", first)
    print("Last digit:", last)
n = int(input("Enter a number: "))
number(n)
