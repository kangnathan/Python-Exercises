height = float(input("Enter Your Height(inches): "))
weight = float(input("Enter Your Weight(pounds): "))

bmi = (weight * 703) / (height**2)
final_bmi = round(bmi,2)


if bmi < 16.0 and bmi > 1:
    print(f"Your BMI of {final_bmi} makes you Severely Underweight")

elif bmi >= 16.0 and bmi <= 18.4:
    print(f"Your BMI of {final_bmi} makes you Underweight")

elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Your BMI of {final_bmi} makes you Normal")

elif bmi >= 25.0 and bmi <= 29.9:
    print(f"Your BMI of {final_bmi} makes you Overweight")

elif bmi >= 30.0 and bmi <= 34.9:
    print(f"Your BMI of {final_bmi} makes you Moderately Obese")
    
elif bmi >= 35.0 and bmi <= 39.9:
    print(f"Your BMI of {final_bmi} makes you Severely Obese")

elif bmi > 39.9 :
    print(f"Your BMI of {final_bmi} makes you Morbidly Obese")

else:
    print("Invalid")