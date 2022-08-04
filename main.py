


from calendar import c
from pickle import NONE
from re import S, T, U
from tkinter.messagebox import NO
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
        print ("Creating contact within contact fields...")
        self.name = input("Enter a name for this contact")
        self.phone_number = input("Enter a phone number for this contact")
        self.email = input("Enter a email address for this contact")


    def create_contact_advanced(self):
        print ("Creating contact advanced within contact fields...")
        self.last_name = input("Enter a last name for this contact")
        self.relationship = input("Enter a relationship for this contact")
        self.status = input("Enter a status for this contact")
        self.work = input("Enter a work for this contact")


    def modification_contact_basic(self):
        print ("Moving contact into contact fields for modify contact...")
        self.name = input("Enter a modified name for this contact")
        self.phone_number = input("Enter a modified phone number for this contact")
        self.email = input("Enter a modified email address for this contact")

    def modification_contact_advanced(self):
        print ("Moving contact into contact advanced for modify contact...")
        self.last_name = input("Enter a modified last name for this contact")
        self.relationship = input("Enter a relationship")
        self.status = input("Enter a modified status for this contact")
        self.work = input("Enter a modified work for this contact")

    def call(self,name):
        print ("Calling to contact: ", name)
        
    
        

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

    def modified_user(self, username, password):
        
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
                x=False
                break
            elif check_3!=self.username or check_2!=self.password:
                print("Your username or your password is incorrect.\n")
                break
            elif check_3 or check_2=="":
                raise TypeError("Please enter your username and passwork corretly: ")



            
        new_user=input("for created account, please type y (yes) or n (no)")
        if new_user=="y":
            self.create_user()
        else:
            print("bye bye!")
        
        
        
        
    


print("Hello to my address book!\n")
user1=login(username="user1", password="password")
user1.check_login()


if __name__ == '__main__':
    pass