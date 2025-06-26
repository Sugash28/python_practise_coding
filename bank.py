def tour_amount_increasing(amount, members):
    members -= 1
    amount += 400
    return amount, members

def tour_amount_decreasing(amount, members):
    members += 1
    amount -= 400
    return amount, members

members = 67
amount = 3000

while True:
    print("1. Willing to come on the tour")
    print("2. Not willing to come on the tour")
    print("3. Exit")
    
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        amount, members = tour_amount_decreasing(amount, members)
        print("Amount is:", amount)
        print("Members are:", members)
    elif choice == 2:
        amount, members = tour_amount_increasing(amount, members)
        print("Amount is:", amount)
        print("Members are:", members)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
