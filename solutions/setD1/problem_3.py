weight, height = map(float, input().split())
bmi = weight / (height ** 2)
bmi_val = round(bmi, 1)

if bmi_val < 18.5:
    category = "Underweight"
elif bmi_val < 25.0:
    category = "Normal Weight"
elif bmi_val < 30.0:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi_val:.1f} | Category: {category}")
