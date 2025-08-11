def showInputs():
    weight = float(input("Enter weight in Kilograms(kg): "))
    height = float(input("Enter height in meters (m): "))
    return weight , height


def BMI():
    
    while True:
        weight, height = showInputs()
        bmi = weight / (height**2)
        print(f"The calculated BMI is {bmi}")
        
        if bmi < 18.5:
            print("You are Underweight")
        elif 18.5 <= bmi <= 24.9:
            print("You have a Normal Weight")
        elif 25 <= bmi <= 29.9:
            print("You are OverWeight")
        else:
            print("You are Obese")
            print("Exiting the Program")
            break


BMI()

