# ATM Simulation
# PIN = 4321, starting balance = Rs. 20000

correct_pin = 4321
balance = 20000

print("----- WELCOME TO ATM -----")

# user gets only 3 attempts for the pin
attempts = 0
logged_in = False

while attempts < 3:
    pin = int(input("Enter your 4 digit PIN: "))
    if pin == correct_pin:
        logged_in = True
        break
    else:
        attempts = attempts + 1
        print("Wrong PIN. Attempts left:", 3 - attempts)

if logged_in == False:
    print("Card blocked! Too many wrong attempts.")
else:
    print("Login successful!")

    # withdraw again and again until user enters 0
    while True:
        amount = int(input("\nEnter amount to withdraw (0 to quit): "))

        if amount == 0:
            print("Thank you for using ATM. Bye!")
            break
        elif amount < 0:
            print("Invalid amount! Amount cannot be negative.")
        elif amount % 500 != 0:
            print("Amount must be a multiple of 500.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Please take your cash.")
            print("Remaining balance: Rs.", balance)

            if balance == 0:
                print("Your balance is now zero. Bye!")
                break
