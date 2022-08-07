


from calendar import c
from pickle import NONE
from re import S, T, U
from unicodedata import name



class contact():

    name=None
    phone_number="12345"
    email="test@example.com"
    
    def __init__(self):
       
        self.last_name = None
        self.relationship = None
        self.status = None
        self.work = None

    def create_contact_basic(self):
        print ("\nCreating contact within contact fields...\n")
        self.name = input("Enter a name for this contact: ")
        self.phone_number = input("Enter a phone number for this contact: ")
        self.email = input("Enter a email address for this contact: ")
        print ("\nCreated contact within contact fields...\n")
        self.option_process()


    def create_contact_advanced(self):
        print ("\nCreating contact advanced within contact fields...\n")
        self.last_name = input("Enter a last name for this contact: ")
        self.relationship = input("Enter a relationship for this contact: ")
        self.status = input("Enter a status for this contact: ")
        self.work = input("Enter a work for this contact: ")
        print ("\nCreated contact within contact fields...\n")
        self.option_process()


    def modification_contact_basic(self):
        print ("\nMoving contact into contact fields for modify contact...\n")
        self.name = input("Enter a modified name for this contact: ")
        self.phone_number = input("Enter a modified phone number for this contact: ")
        self.email = input("Enter a modified email address for this contact: ")
        print ("\nModified contact within contact fields...\n")
        self.option_process()

    def modification_contact_advanced(self):
        print ("\nMoving contact into contact advanced for modify contact...\n")
        self.last_name = input("Enter a modified last name for this contact: ")
        self.relationship = input("Enter a relationship: ")
        self.status = input("Enter a modified status for this contact: ")
        self.work = input("Enter a modified work for this contact: ")
        print ("\nModified contact within contact fields...\n")
        self.option_process()

    def call_contact(self,name):
        print ("Calling to contact: ", name)
        x=input("For finish your call_contact type *F*: ")
        if x == "F":
            print ("your call_contact is end")
            self.option_process()    

    def option_process(self):
        option1=None
        print("selected option")
        option1= input("""\n Enter the number of option tha you want to process: 
        1- Create a new contact with basic information
        2- Create a new contact with advanced information
        3- modify a the contact with basic information
        4- modify a the contact with advanced information
        5- call a contacts
        6- for exit of system tipe *x*\n""")

        if option1 =="1":
            self.create_contact_basic()
        elif option1 =="2":
            self.create_contact_advanced()
        elif option1=="3":
            self.modification_contact_basic()
        elif option1 =="4":
            self.modification_contact_advanced()
        elif option1 =="5":
            calling_for_contact=input("Enter the name of the contact: ")
            self.call_contact(calling_for_contact)
        elif option1 =="x":
            exit()


    
        

class login(contact):
    
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
    
    def create_user(self):
        
        print ("Creating user...")
        self.username =input("Enter username: " )
        self.password=input("Enter password: " )
        print ("created user...")
        self.check_login()

    def modified_user(self):
        
        print("Modifing user...")
        check_1=input("please enter username to verify")
        if check_1==self.username:
            self.__password=input("Please enter: ")
            print("User modify successfully\n")
        elif check_1!=self.username:
            print("your are not allowed to modify this user\n")
        else:
            if check_1=="":
                raise TypeError("Please enter you can enter a blank username")  

    def check_login(self): 
        x= True
        while x == True:
            print ("Checking login...")
            check_3=input("Please enter your username: ")
            check_2=input("Please enter your passwork: ")
            if check_3==self.username and check_2==self.password:
                print ("Checking password...")
                print("WELLCOME\n")
                self.option_process()
                x=False
            elif check_3!=self.username or check_2!=self.password:
                print("Your username or your password is incorrect.\n")

                new_user=input("for created account, please type y (yes) or n (no)")

                if new_user=="y":
                    self.create_user()
                else:
                    print("bye bye!")
                break
            elif check_3 or check_2=="":
                raise TypeError("Please enter your username and passwork corretly: ")

          
                
        
        
        
        
    


print("Hello to my address book!\n")
user1=login(username="user1", password="password")
user1.check_login()
contacts=contact()


if __name__ == '__main__':
    pass