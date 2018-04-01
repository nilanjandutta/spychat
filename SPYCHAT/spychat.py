from spy_base import spy
from steganography.steganography import Steganography
from datetime import datetime
date = datetime.now()
print date
print "Hello detective"
print "Welcome to the spy world!"
print "Let\'s get started"

status_message = ["Today is very Beautiful","Good Morning!","Stay disconnected"]
friends=[{'name': 'Johnny','age':22,'rating':3.5,'is_online':True},{'name': 'Sparrow','age':24,'rating':2.5,'is_online':True}]

def add_status(a_status):
    if a_status != None:
        print "Your current status is " + a_status
    else:
        print "You Don\'t have any status currently"
    existing_status = raw_input("You want select an old status? Y/N")
    if existing_status.upper() == "N":
        new_status = raw_input("Enter your status ")
        if len(new_status)>0:
            status_message.append(new_status)

    elif existing_status.upper()=='Y':
        serial_no = 1
        for old_status in status_message:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice=input("Enter your choice ")
        new_status=status_message[user_choice-1]
        updated_status=new_status
        return updated_status

def add_friend():
    friend = {
        'name': ". ",
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    friend['name']=raw_input("What is Your Name? ")
    friend['age']=input("What is your age? ")
    friend['rating']=input("What is your current spy rating? ")
    if len(friend['name'])>2 and 50>(friend['age'])>5 and friend['rating']>spy['rating']:
        friends.append(friend)
    else:
        print("Sorry! Friend cannot be added ")
    return len(friends)

def select_friend():
    serial_no = 1
    for friend in friends:
        print str(serial_no) + "  " + friend['name']
        serial_no = serial_no + 1
    user_selected_friend = input("Enter your choice : ")
    user_selected_friend_index = user_selected_friend -1
    return user_selected_friend_index

#defining function send_message
def send_message():
    selected_friend = select_friend()
    original_image = raw_input(" What is the name of your original image? ")
    secret_text = raw_input(" What is your secret text? ")
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,secret_text) #call from Stegnography library
    print "your message is encoded"

#defining function read_message
def read_message():
    selected_friend = select_friend()
    output_path = raw_input("Which image you want to decode? ")
    secret_text = Steganography.decode(output_path)
    print "Secret text is : " + secret_text


#defining funtion lets_chat
def lets_chat(spy_name,spy_age,spy_rating):
    print("Here are your options : ") + spy_name
    current_status = None
    show_menu = True
    while show_menu:
        choice=input("What do you want to do? \n 1.Add a status \n 2. Add a Friend \n 3. Send a Message \n 4. Read a message \n 0. Exit")
        if choice == 1:
            current_status = add_status(current_status)
            print "Updated status is : " + current_status
        elif choice == 2:
            no_of_friends = add_friend()
            print "You have " + str(no_of_friends) + "friends"
        elif choice == 3:
            send_message()
        elif choice == 4:
            read_message()

        elif choice == 0:
            show_menu=False
        else:
            print " Invalid Input "


spy_exist=raw_input("Are You a new user? Y/N ")


if spy_exist.upper()=="N":
    print "Welcome Back " + spy['name'] + " age : " + str(spy['age']) + " rating: " + str(spy['rating'])
    lets_chat(spy['name'],spy['age'],spy['rating'])

elif spy_exist.upper()=="Y":
    spy={
        'name': " ",
        'age':0,
        'rating' :0.0
    }



    spy['name']=raw_input("What is your name? ")
    if len(spy['name'])>2:
        print "Welcome" + spy['name'] + "Glad to see you!"
        spy_salutation=raw_input("What should we call you? Mr/Ms")
        if spy_salutation=="Mr." or spy_salutation=="Ms.":
            spy['name']=spy_salutation + " " + spy['name']
            print "Great! " + spy['name'] + " Tell us some more about you.."
            spy['age']=input("What is your age? ")
            if 55>spy['age']>5:
                print "Your passed the age criteria"
                spy['rating']=input("What is your current spy rating? ")
                if spy['rating']>=5.0:
                    print "Outstanding spy"
                elif 5.0>spy['rating']>=4.0:
                    print "Great Spy"
                elif 4.0>spy['rating']>=3.0:
                    print "Average spy"
                elif 3.0>spy['rating']>=2.0:
                    print "You are on your border line"
                else:
                    print "Sorry! You are not suitable for this"
                spy_is_online=True
                print "Authentication Complete! Welcome " + spy['name'] + "Age: "+ str(spy['age'])+ "Having a Rating of :" + str(spy['rating'])
                lets_chat(spy['name'],spy['age'],spy['rating'])
            else:
                print "You are too small or too old to be trained"
        else:
            print "Oops Invalid Entry! "
    else:
        print "Sorry! You Entered an Incorrect Name"
else:
    print "Invalid Entry"














