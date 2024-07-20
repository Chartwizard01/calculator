print("WELCOME TO FITHEALTH, INPUT THE REQUIRED DETAILS TO CHECK YOUR BMI")


#collecting the weight and height details of user in order to use and calculate the bmi
weight = float(input("what is your weight(KG)?:  "))

height = float(input("what is your height (Meters)?:  "))


#we first collect result of the operation so we can use round command to round up to 1 dp
result = weight/ (height*height)

#our bmi is now result rounded to one decimal place
bmi = round(result, 1)

#these are our if-elif-else commands to help us screen different outcomes and print the corresponding message 
if bmi<18.5 :
    print("you are underweight")

elif bmi > 18.5 and bmi<=24.9:
    print(" you are normal")


elif bmi > 24.9 and bmi <=29.9 :
    print("you are overweight")

elif bmi > 29.9 and bmi<=34.9 :
    print("you are OBESE")

elif bmi>= 35:
    print("your case is extreme, consult a doctor today!!!")

else:
    print("wrong entry")
print(f"your bmi is {bmi}" )