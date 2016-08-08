def get_gender(sex="Unknown"): #set the default value of sex to "Unknown" if not set
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()