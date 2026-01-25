#some base Math for Ptyhon :)
#Base
#Addition is used to add Numbers example:
print("Addition")
print(5 + 1)
print(5 + 9)
print(3112 + 982)

#Subtraction is used to subtract Numbers example:
print("Subtraction")
print(5 - 1)
print(294 - 135)
print(92 - 12)
print(9484923 - 29482)

#Multiplication is used to multiply Numbers example:
print("Multiplication")
print(10 * 9)
print(129 * 12)
print(19384 * 1234)

#Division is used to divide Numbers example:
print("Division")
print(5 / 3)
print(99 / 33)
print(1920 / 123)

# we use // to figure out how many times the first number fits into the second example:
print("Whole Number Division")
print(6 // 2)
print(900 // 2)
print(340 // 120)

#when we use // we ony get full Numbers so theres a Rest if it isnt divisible. To find the rest e use % example:
print("Modulo")
print(3 % 2)
print(340 % 120) #example 340 // 120 returns 2 so 120 fits twice in 340 and the Modulo % returns 100 so 100 is left after 120 is fit 2 in 340
print(9200000 % 401)


#Number Analysis combining them in a little script that takes input converts to int and then shows some data :)
A = int(input("Enter your first number: "))
B = int(input("Enter your second number: "))
print(f"Your numbers are {A} and {B}")
print(f"Division result = {A / B}")
print(f"Whole Division: {A // B}")
print(f"Remainder = {A % B}")