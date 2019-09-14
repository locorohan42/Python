#Rohan Abraham
#Code will take in an amount of seconds and convert to
#minutes, hours and days.

timeInput = int(input("Enter a number of seconds: "))
print("Time will be displayed by days, hours, minutes and then seconds.")

seconds = timeInput % 86400 % 3600 % 60
hours = timeInput / 60
minutes = hours % 60
hours = hours / 60
days = timeInput / 86400

print(int(days))
print(int(hours))
print(int(minutes))
print(int(seconds))

