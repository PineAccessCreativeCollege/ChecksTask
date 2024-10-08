correctISBN = "9781861972712"
isbnSD = 0
addedISBN = 0
moduloISBN = 0
checkDigit = 0
itBool = True

print("This program will generate a check digit for testing purposes")

ISBNNumber = input("Please enter your ISBN number (12 characters): ")

ISBNLen = len(ISBNNumber)

if ISBNLen == 12:
    print("ISBNCorrect")

    for c in ISBNNumber:
        #isbnSD = int(c)
        #print(c)
        if itBool == True:
            addedISBN += int(c)*1
        elif itBool == False:
            addedISBN += int(c)*3

        itBool = not itBool
        #print(addedISBN)

    moduloISBN = addedISBN % 10
    if moduloISBN != 0:
        checkDigit = 10 - moduloISBN
        print(checkDigit)
else:
    print("incorrect ISBN")



