
def checkValue(square) :

	while True:
		value = input(f"{square}:  ")

		if not value.isdigit():
			print("You should enter the digit!")
			continue

		elif int(value) > 8 or int(value) < 1:
			print("You should enter the digit between 1-8!")
			continue

		x1 = int(value)
		
		return value

x1=checkValue("X1")
x2=checkValue("X2")
y1=checkValue("Y1")
y2=checkValue("Y2")



