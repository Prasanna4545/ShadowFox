height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi >= 30:
    print("Obesity")

elif bmi >= 25:
    print("Overweight")

elif bmi >= 18.5:
    print("Normal")

else:
    print("Underweight")

# Question 2

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter city name: ")

if city in Australia:
    print(city, "is in Australia")

elif city in UAE:
    print(city, "is in UAE")

elif city in India:
    print(city, "is in India")

else:
    print("City not found")

# Question 3

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

if city1 in India and city2 in India:
    print("Both cities are in India")

elif city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")

elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")

else:
    print("They don't belong to the same country")        