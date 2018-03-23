print "hello detective!"
print "Let's get started! "
print "Are You ready to enroll?"
First_name = raw_input(" What is your first Name ")
if not First_name.isalpha():
    print("Sorry!, Only letters are allowed!")
Last_name =raw_input (" What is your Last Name ")
if not Last_name.isalpha():
    print("Sorry!, Only letters are allowed!")
spy_name1 = "Your spy name is: " + First_name+ " " +Last_name
spy_name=  First_name+ " " +Last_name
if len(spy_name)>3:
    print " Welcome " + spy_name + ",Happy to have you with us! "
    spy_salutation = raw_input(" What should we call you? (Mr. or Ms.) ")
    if spy_salutation == "Mr." or spy_salutation == "Ms.":
        spy_name = spy_salutation + " " + spy_name
        print " Ok! " + spy_name + " Let us hear little more about you."
        spy_age = input(" What is your age? ")
        if 55>spy_age>10:
            print " You qualify your age criteria. "
            spy_rating = input(" What is your current Rating? ")
            if spy_rating>=5.0:
                print " Outstanding record! "
            elif 5.0>spy_rating>=3.0:
                print " Good! Need Perfection "
            elif 3.0>spy_rating>2.0:
                print " Below Average! "
            else:
                print " How are you still competing? "
            spy_online= True
            print "Authentication completed, Welcome!" + spy_name + " age: " + str(spy_age) + " With a Rating of: " + str(spy_rating) + " Glad to have you onboard!"
        else:
            print "Sorry! You are too young or too old to be trained."
    else:
        print "Invalid Salution, try Again!"
else:
    print "Oops Soory, Please Enter a valid Name!"

