gpa = float(input("What is your unweighted GPA? " ))
hours = int(input("How many service hours do you have? "))

if gpa >= 3.5:
    if hours > 50:
        print("Eligible for scholarship. ")
    elif (hours >= 30) and (hours <= 50):
        print("Eligible for partial scholarship.")
    else:
        print("You need more hours.")
elif (gpa >= 3.0) and (gpa < 3.5):
    if hours > 50:
        print("Eligible for partial scholarship.") 
    else: 
        print("Need more hours to be eligible for scholarship.") 
else:
    print("Not eligible for scholarships.")      
        