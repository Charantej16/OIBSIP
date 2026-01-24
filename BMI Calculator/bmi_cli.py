print("=== Welcome to BMI Calculator ===")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("❌ Weight and height must be positive numbers")
        exit()

    bmi = weight / (height * height)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("Your BMI is:", bmi)
    print("Health Category:", category)

except ValueError:
    print("❌ Please enter valid numeric values")                    