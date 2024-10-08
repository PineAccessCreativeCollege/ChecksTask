import re
uUID = input("Input User ID eg[Aab123]: ")

regExpression = re.compile("^[A-Z][a-z]{2}[0-9]{3}$")

if regExpression.match(uUID):
    print("correct")
else:
    print("Incorrect")

