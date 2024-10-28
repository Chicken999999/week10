gpa = float(input("What is your unweighted GPA? " ))
hours = int(input("How many service hours do you have? "))

if gpa >= 3.5: #checks if gpa is greater or equal to 3.5
    if hours > 50: #checks if hours are greater than 50 if gpa is greater or equal to 3.5
        print("Eligible for scholarship. ")
    elif (hours >= 30) and (hours <= 50): # checks if hours is between 30 and 50 if gpa is greater or equal to 3.5
        print("Eligible for partial scholarship.")
    else:
        print("You need more hours.")
elif (gpa >= 3.0) and (gpa < 3.5): #if gpa is between 3 and 3.5
    if hours > 50: #checks if hours are over 50
        print("Eligible for partial scholarship.") 
    else: #true if hours are 50 or below
        print("Need more hours to be eligible for scholarship.") 
else: #if gpa below 3.0, this is true
    print("Not eligible for scholarships.")      
        