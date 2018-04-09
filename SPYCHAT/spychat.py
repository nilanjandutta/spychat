import sys
sys.stdout.write("\033[1;31m")
print "All following prints will be red ..."
from spy_base import spy, Spy,ChatMessage
from steganography.steganography import Steganography #from stegnography library and stegnography object , Stegnography module is called
from datetime import datetime #gives the current date and time
import csv

date = datetime.now()
print date
print "Hello detective"
print "Welcome to the spy world!"
print "Let\'s get started"

def ask():
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    checkpassword(username, password)
def checkpassword(use, pwd):
    if use == "python" and pwd == "spychat":
        login(use)
    else:
        print "Your username and/or password was incorrect"
        ask()
def login(use):
    print "Welcome " + use
    print "You have successfully logged in!"
ask()

status_message = ["Today is very Beautiful","Good Morning!","Stay disconnected"]
friend1=Spy("John","Mr.",25,3.3)
friend2=Spy("Mohan","Mr.",29,3.9)
friends=[friend1,friend2]
messages=[]

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)
        next(reader)

        for row in reader:
            friend = Spy(name=row[0],salutation=row[1],age=[2],rating=[3])
            friends.append(friend)

load_friends()

def load_messages():
    with open('messages.csv', 'rb') as message_data:
        reader = csv.reader(message_data)
        next(reader)

        for row in reader:
            message = Spy(sender_name=row[0],message=row[1])
            messages.append(message)

load_messages()

def read_chat_history():
    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print('[%s]' % chat.time.strftime("%d %B %Y"))
            print('%s' % 'you said : ')
            print '%s' % chat.message
        else:
            print('[%s]' % chat.time.strftime("%d %B %Y"))
            print('%s said : ' % friends[read_for].name)
            print '%s' % chat.message


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

    elif existing_status.upper()== 'Y':
        serial_no = 1
        for old_status in status_message:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice=input("Enter your choice ")
        new_status=status_message[user_choice-1]
        updated_status=new_status
        return updated_status

#definining method add_friend
def add_friend():
    friend = Spy("","",0,0.0)
    friend.name = raw_input(" What is Your Name? ")
    friend.salutation = raw_input("What should we call you? ")
    friend.age = input(" What is your age? ")
    friend.rating = input(" What is your current spy rating? ")
    friend.is_online = True
    if len(friend.name)>2 and 50>(friend.age)>5 and friend.rating>spy.rating:
        with open('friends.csv','a')as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow( [friend.name, friend.salutation, friend.age, friend.rating, friend.is_online] )
    else:
        print("Sorry! Friend cannot be added ")
    return len(friends)

#defining function select_friend
def select_friend():
    serial_no = 1
    for friend in friends:
        print str(serial_no) + "  " + friend.name
        serial_no = serial_no + 1
    user_selected_friend = input("Enter your choice : ")
    user_selected_friend_index = user_selected_friend -1
    return user_selected_friend_index

#defining function send_message
#sending message with the help of stegnography module , a secret encoded message in an image
def send_message():
    selected_friend = select_friend()
    original_image = raw_input(" What is the name of your original image? ")
    secret_text = raw_input(" What is your secret text? ")
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,secret_text) #call from Stegnography library
    new_chat = ChatMessage(secret_text,True)
    friends[selected_friend].chats.append(new_chat)
    with open('messages.csv', 'a')as message_data:
        writer = csv.writer(message_data)
        writer.writerow([secret_text])
    print "You made a secured message!"


#defining function read_message
def read_message():
    selected_friend = select_friend()
    output_path = raw_input("Which image you want to decode? ")
    secret_text = Steganography.decode(output_path)
    print "Secret text is : " + secret_text
    new_chat= ChatMessage(secret_text,False)

    friends[selected_friend].chats.append(new_chat)
    print("Your Secret Message has been saved")


#defining funtion lets_chat
def lets_chat(spy_name,spy_age,spy_rating):
    print("Here are your options : ") + spy_name
    current_status = None
    show_menu = True
    while show_menu:
        choice=input("What do you want to do? \n 1.Add a status \n 2. Add a Friend \n 3. Send a Message \n 4. Read a message \n 5. Read Chat History \n 0. Exit")
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
        elif choice == 5;
            read_chat_history()

        elif choice == 0:
            show_menu=False
        else:
            print " Invalid Input "


spy_exist=raw_input("Are You a new user? Y/N ")  #choose you are new user or old


if spy_exist.upper()=="N":
    print "Welcome Back " + spy.name + " age : " + str(spy.age) + " rating: " + str(spy.rating)
    lets_chat(spy.name,spy.age,spy.rating) #details are being called from dictionary

elif spy_exist.upper()=="Y":
    spy= Spy("","",0,0.0)



# gives the details of a new spy
    spy.name=raw_input(" What is your name? ")
    if len(spy.name)>2:
        print " Welcome " + spy.name + " Glad to see you! "
        spy_salutation=raw_input(" What should we call you? Mr/Ms ")
        if spy_salutation=="Mr." or spy_salutation=="Ms.":
            spy.name=spy_salutation + " " + spy.name
            print " Great! " + spy.name + " Tell us some more about you.."
            spy.age=input(" What is your age? ")
            if 55>spy.age>5:
                print " Your passed the age criteria "
                spy.rating=input(" What is your current spy rating? ")
                if spy.rating>=5.0:
                    print " Outstanding spy "
                elif 5.0>spy.rating>=4.0:
                    print " Great Spy "
                elif 4.0>spy.rating>=3.0:
                    print " Average spy "
                elif 3.0>spy.rating>=2.0:
                    print " You are on your border line "
                else:
                    print " Sorry! You are not suitable for this "
                spy_is_online=True
                print "Authentication Complete! Welcome " + spy.name + "Age: "+ str(spy.age)+ "Having a Rating of :" + str(spy.rating)
                lets_chat(spy.name,spy.age,spy.rating)
            else:
                print "You are too small or too old to be trained"
        else:
            print "Oops Invalid Entry! "
    else:
        print "Sorry! You Entered an Incorrect Name"
else:
    print "Invalid Entry"














