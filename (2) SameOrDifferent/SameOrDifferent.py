name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age == 14 and name == "Arhan":
    print("We have the same name and age.")
elif age == 14 and len(name) == 5:
    print("We have the same age and our names are the same length.")
elif age > 14 and name != "Arhan":
    print("You are older than me and have a different name")
elif age < 14 and name != "Arhan":
    print("You are younger than me and you have a different name.")
else: 
    print("We share nothing in common. (Different)")
   
