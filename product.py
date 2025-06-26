product=1
for number in range(1, 201):
    if number % 11 == 0 and number % 9 == 0:
        print(number)
        product *= number 
        print(f"{number} is divisible by both 11 and 9. Product: {number}")
print(product)