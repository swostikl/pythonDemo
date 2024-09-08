import math

print("Hello! World")

#Inputs, variables and assignment-statements
# Ask user a name and greet the user by their name
user_name = input("Enter your name: ")
print(" Good morning", user_name)

# calculation of temperature in Fahrenheit and convert into Celsius
temperature=float(input("Enter your temperature(in Fahrenheit): "))
celsius=(temperature-32)*5/9
print(f"The fahrenheit {temperature} temperature into celsius is ,{celsius:.2f}")

#math.pi and math.e
print(f"{'pi':12s}:{math.pi:10.5f}")
print(f"{'e':12s}:{math.e:10.5f}")

# conditional statement (if)
# buy a cafe latte which cost 5 euros and check whether you have enough money to buy latte.
Money=float(input("Enter the money you have (in euros): "))
if Money>=5:
    print("Buy latte")
else:
    print("Not enough money")


# check whether the medicine can be given to patient or not
# Age at least 15 and weight must 55
# if age is at least 15 and less than 18, program also ask the weight

age=int(input("Enter your age: "))
if 15<=age<=18:
    weight = float(input("Enter your weight(in kg) : "))
    if age>=15 or age>=18 and weight>=55:
        print("Medicine can be given to a patient")
else:
    print(" sorry medicine can not be given to patient")

# Ask the user's age and notify them whether they are retired, working/age, in school or a small child.
#age more than 65 retired
# age between 18 and 65 working-age
# age between 7 and 18 is school-child
# age between 6 and 0 child

age=int(input("Enter your age: "))
if age>=65:
    print("You are a retired")
elif age>=18:
    print("You are in working-age")
elif age>=7:
    print("You are in school")
else:
    print("You are a child")

