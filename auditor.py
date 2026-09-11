from logging import warning

inventory = int(0)

userInput = ""

while userInput != "quit":
    userInput = input("Enter a stock quantity: ")
    if userInput == "quit":
        print("Goodbye!")
        break
