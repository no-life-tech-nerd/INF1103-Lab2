from logging import warning

inventory = int(0)

userInput = ""

while userInput != "quit":
    userInput = input("Enter a stock quantity: ")
    if userInput == "quit":
        print("Goodbye!")
        break
    try:
        addedInventory = int(userInput)
        if addedInventory < 0:
            warning("Negative number not accepted, try again!")
    except:
        warning(f"Input of type {str(type(userInput))} not accepted, try again!")
        continue
