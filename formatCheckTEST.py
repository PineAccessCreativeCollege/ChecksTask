from datetime import datetime

format = "%d-%m-%Y"

date = input("Enter the date in format: 'day-month-year' year should have 4 digits.")

res = True

try:
    res = bool(datetime.strptime(date, format))
except ValueError:
    res = False

if res == False:
    print("Date Does Not Match Format: [d-m-Y]")

elif res == True:
    print("Date matches Format")