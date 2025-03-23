import random

while True:
    choice = input("Roll the Dice (yes/No): ").strip().lower()
    
    if choice == "yes":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, {die2}")
    elif choice == "no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice! Please enter 'yes' or 'no'.")
