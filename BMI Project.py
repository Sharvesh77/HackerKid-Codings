Weight = float(input("Enter the weight: "))
Height = float(input("Enter the Height"))
BMI = Weight/Height**2
print (BMI)
if BMI<=18.5:
    print("You are Underweight")
elif 18.5<BMI and BMI<=24.9:
    print("Normal Weight")
elif 25<=BMI and BMI<=29.9:
    print("You are Overweight")
elif BMI>29.9:
    if 30<=BMI and BMI<=34.9:
        print("Moderate Obesity")
    elif 35<=BMI and BMI<=39.9:
        print("Severe Obesity")
    else:
        print("Very Severe Obesity")
else:
    print("Enter the Correct BMI value")
