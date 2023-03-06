name = input("Enter your name ")
weight = int(input("Input weight in pounds: "))
height = float(input("Input height in inches: "))

bmi = (weight * 703) / (height * height)

if bmi <= 18.5:
    print(f'Hi {name} your BMI is {bmi}. You are underweight with minimal health risk')
elif bmi >= 18.5:
    print(f'Hi {name} your BMI is {bmi}. You are normal weight with minimal health risk')
elif bmi >= 25:
    print(f'Hi {name} your BMI is {bmi}. You are overweight with increased health risk')
elif bmi >= 30:
    print(f'Hi {name} your BMI is {bmi}. You are obese with high health risk')
elif bmi >=35:
    print(f'Hi {name} your BMI is {bmi}. You are severely obese with very high health risk')
else:
    print(f'Hi {name} your BMI is {bmi}. You are Morbidly obese with extremely high health risk')