#inputs
name = input("What is your name?")
height = float(input("What is your height in cm?"))
weight = float(input("What is your weight in kg? "))

#name
namesent = "Hello, %s"
namesentend = namesent + "!"
namesentfinal = (namesentend % (name))
print(namesentfinal)

#bmi 
heightm = height * 0.01
heightsq = heightm ** 2
bmiresult = weight / heightsq
bmisent ="Your bmi is %f"
bmir = round(bmiresult)
print("Your Bmi rounded is:", bmir)
print(bmisent % (bmiresult))
if bmiresult <18.5:
    print("You are underweight")
elif bmiresult >18.5:
    print("You are in the average weight class")
elif bmiresult >25:
    print("You are overweight!")
elif bmiresult >30:
    print("You are obese")

#protein
weightp = weight * 2.2
proteinsent = "You need %fg of protein everyday to maximise muscle gain"
print(proteinsent % (weightp))







      




