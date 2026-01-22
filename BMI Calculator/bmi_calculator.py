def calculate_bmi(weight, height):
    """
    Calculates BMI using the standard formula.
    BMI = weight (kg) / (height (m))^2
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    """
    Determines BMI category based on value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_user_input():
    """
    Takes valid weight and height input from user.
    """
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))

            if weight <= 0 or height <= 0:
                print("❌ Weight and height must be positive numbers.")
                continue

            return weight, height

        except ValueError:
            print("❌ Please enter valid numeric values.")


def display_result(bmi, category):
    """
    Displays BMI result and health category.
    """
    print("\n📊 BMI RESULT")
    print("---------------------")
    print(f"Your BMI Value : {bmi}")
    print(f"Health Status : {category}")
    print("---------------------")


def main():
    print("================================")
    print("        BMI CALCULATOR           ")
    print("================================")

    while True:
        weight, height = get_user_input()

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        display_result(bmi, category)

        choice = input("\nDo you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            print("\nThank you for using BMI Calculator 👍")
            break


if __name__ == "__main__":
    main()
