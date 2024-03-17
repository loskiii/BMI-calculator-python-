def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = weight / ((height/100) ** 2)  # Convert height to meters
        return bmi
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An error occurred: {e}"

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = input("Enter your weight in kilograms: ")
    height = input("Enter your height in centimeters: ")

    bmi = calculate_bmi(weight, height)
    if isinstance(bmi, float):
        print(f"Your BMI is: {bmi:.2f}")
    
        bmi_category = interpret_bmi(bmi)
        print(f"You are classified as: {bmi_category}")
    else:
        print(bmi)

if __name__ == "__main__":
    main()
