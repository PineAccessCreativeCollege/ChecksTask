##range 1 - 100

enteredNumber = int(input("Enter a number between 1 and 100: "))

def TrueDef1():
    print("IN Range")


def FalseDef1():
    print("OUT Range")

if enteredNumber >= 1 & enteredNumber <= 100:
    TrueDef1()
else:
    FalseDef1()
