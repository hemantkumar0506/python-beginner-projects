mass = int(input("Your mass in KG = "))
height = int(input("Your height in CM = "))

def bmi_calculator(mass, height):
    BMI = (mass / height**2) * 10000
    return BMI

bmi_score = bmi_calculator(mass, height)
if 0 < bmi_score < 16.0:
    print(f"Your BMI Score is {bmi_score}. You have Severe Thinness")
elif 16.0 < bmi_score <= 17.0:
    print(f"Your BMI score is {bmi_score}. You have Moderate Thinness")
elif 17.0 < bmi_score <=18.5:
    print(f"Your BMI score is {bmi_score}. You have Mild Thinness")
elif 18.5 < bmi_score <= 25.0:
    print(f"Your BMI score is {bmi_score}. You are Normal")
elif 25.0 < bmi_score <= 30.0:
    print(f"Your BMI score is {bmi_score}. You are Overweight")
elif 30.0 < bmi_score <= 35.0:
    print(f"Your BMI score is {bmi_score}. You have Obese Class I")
elif 35.0 < bmi_score <= 40.0:
    print(f"Your BMI score is {bmi_score}. You have Obese Class II")
elif bmi_score > 40.0:
    print(f"Your BMI score is {bmi_score}. You have obese Class III")
else:
    print("enter valid details")