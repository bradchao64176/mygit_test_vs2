
hieght = int(input("please input your hieght:"))
weight = int(input("please input your wieght:"))
bmi = weight / ((hieght/100) **2)
print("BMI={:.2f}".format(bmi))

if bmi < 18.5:
    print("BMI is under weight")
elif bmi <25:
    print("BMI is normal weight")
elif bmi <30:
    print("BMI is overweight")
elif bmi < 35:
    print("BMI is obese")
else:
    print("BMI is clinically obese")