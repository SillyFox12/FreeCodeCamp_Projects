def name_gender_transaltor(gender, name):
    if gender == "male" and name == "Jackie":
        return("Jack")
    
    elif gender == "male" and name == "Karen":
        return("Terry")

    elif gender == "male" and name == "Dorothy":
        return("Theodore")

    elif gender == "female" and name == "Thomas":
        return("Thomasina")

    elif gender == "female" and name == "Robert":
        return("Roberta")

    elif gender == "female" and name == "David":
        return("Devetta")

    else:
        return("Please choose an appropriate input.")


gender = input("What gender would you to transelate a name to?")
name = input("What name would you like to transelate?")
result = name_gender_transaltor(gender, name)

print("Your result is: " + result)



    
