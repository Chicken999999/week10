#while loops = execute some code WHILE some condition remains true; could run forever 

##Example 1
# name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name.")
# else:
#     print(f"Hello, {name}")

#iteration = loops
# while name == "":
#     print("You did not enter your name.")
#     name = input("Enter your name: ")

# print(f"Hello, {name}")


##Example 2
# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

##Example 3
# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

##Example 4
# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid ")
#     num = int(input("Enter a number between 1 - 10: "))

# print(f"Your number is {num}")


################# FOR LOOPS #########################

# for loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, 



##EXAMPLE 1

#prints all number within the range. (First number is inclusive, and last is exclusive )
# for x in reversed(range(1, 11)):
#     print(x)
# print("HAPPY NEW YEAR!")


#EXAMPLE 2
# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

#EXAPLE 3 (continue and break)
# for x in range(1, 21):   #skips number 13
#     if x == 13:
#         continue # keeps the code running; skips 13 and keeps code runnig
#     else:
#         print(x)

# for x in range(1, 21):   #stops at number 13
#     if x == 13:
#         break #stops the loop at the inputed value; stops at 12 because it doesn't print when x is 13
#     else:
#         print(x)

################# CHALLENGE #########################

#1)

list_of_names =['John', 'Paul', 'George', 'Ringo']
#if the name is 'Gerorge', print geroge was found 
#oterwise, prinot george was not found and print out other names using a loop 

# for name in list_of_names:
#     if name == "George":
#         print("George was found!")
#     else: 
#         print("George was not found.")
#         print(name)

#2)

list_of_names2 = ["thanos", "Ironman", "Thor", "Hulk"]
#loop through the list andif the name is ironman, skip over it and print out the othe rnames

# for name in list_of_names2:
#     if name == "Ironman":
#         continue       
#     print(name)


#when it encounters thanos, replace its name
# for name in list_of_names2:
#     if name == "thanos":
#        name = "Chicken" #replaces thanos with chicken and prints chicken instead of thanos
#     print(name)

#another way of changing it
for i in range(len(list_of_names2)):
    if list_of_names2[i] == "thanos":
        list_of_names2[i] = "Black Widow"
    print(list_of_names2[i])

