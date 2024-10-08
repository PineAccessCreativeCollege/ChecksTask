passValid = None
inputPass = input("Please Enter Your New Password: ")

passLen = len(inputPass)
print(passLen)

if (passLen<=25 & passLen >=8):
    passValid = True
else:
    passValid = False


if (passValid == True):
    print("Validated")
elif (passValid == False):
    print("INVALID!!!")
