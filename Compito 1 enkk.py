name = input("insert your name here: ")
last_name = input("insert you last name here: ")
age = int(input("insert your age here: "))
#read from the key a name, last name and the age of a person

if len(name) and len(last_name) >1 and age >= 18:
    print("welcome to our casino online!!")
    print("we are so happy to have you here", name.capitalize(), last_name.capitalize())
#if all this are verified the access is garanteed. 
elif len(name) <= 1:
    print("Please insert your real name!")
#we infrom the person that the len of the name is too short
elif len(last_name) <=1: 
    print("Please insert your real last name!")
#same as before 
elif age < 18:
    year_for_18 = 18 - age 
    print("You are too young for gambling, you can be back in", year_for_18, "year")  
#gambiling befor 18 years old is outlaw, so we inform the client to be back in the right years that separets him from the 18 yers old
 