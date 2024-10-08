finishedEnter = False

def NameInput():
    nameInput = input("Enter your Name: ")
    return nameInput

while finishedEnter == False:
    nameInput = NameInput()
    if (any(not c.isalnum() for c in nameInput)):
        print("No special characters are accepted")
    else:
        finishedEnter = True

print("Your name is confirmed and is: " + nameInput)