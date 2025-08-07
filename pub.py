#This is a program for bar and pub restaurant management system.
print("Welcome to the Bar and Pub ")
name = input("Can I know your name? ")
Gender = input("What is your gender? ")
Age = int(input("What is your age? "))
if Age < 18:
    print("Sorry, you are not allowed to enter the bar.")
else:
    print(f"Welcome {name} to the Bar and Pub!")
    print("Here is the menu:")
    print("1. Beer ")
    print("2. Wine ")
    print("3. Whiskey")
    print("4. Cocktails ")
    
    choice = input("What would you like to order? (Enter the number) ")
    
    if choice == '1':
        print("You ordered a Beer.")
    elif choice == '2':
        print("You ordered a Wine.")
    elif choice == '3':
        print("You ordered a Whiskey.")
    elif choice == '4':
        print("You ordered a Cocktail.")
    else:
        print("Invalid choice. Please try again.")

    print("Thank you for visiting the Bar and Pub!")
    print("Have a great time!")
    print("Please drink responsibly.")
