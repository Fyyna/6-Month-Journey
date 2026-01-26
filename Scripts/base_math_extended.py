#going a bit deeper into base math and exploring shit



#add an input for modularity
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))



#Doubling Numbers is easy just multiply by 2 trippling adn so in is logical
print(f"{num1} double is: {num1 * 2}")

#halving is the oposite of doubling so we swap multiplication with division
print(f"{num1} halves is {num1 / 2}")

#How many times num 2 fits into num 1
print(f"{num2} fits {num1 // num2} in {num1}")

#remainder is whats left after weve did modulo
print(f"after distributing into chunks of {num2} we have {num1 % num2} left")

#producing a float with operation
print(f"when we divise we get a float like this when we divise {num1} by {num2} we get {num1 / num2}")

#producing an integer
print(f"when we use base operations like + * - we get integers like when we multiply {num1} by {num2} we get {num1 * num2}")

#a bit more complicated print :P
print(f"If we divide {num1} by {num2} we get {num1 / num2}. But if we need the whole number we get {num1 // num2} and the remainder will be {num1 % num2}")

#check if numbers still correct
num1 == (num1 // num2) * num2 + (num1 % num2)