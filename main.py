


from calendar import c
from re import S, T
from unicodedata import name



class contact():

    name=None
    phone_number="12345"
    email="test@example.com"
    
    def __init__(self,last_name=None, relationship=None, status=None, work=None):
       
        self.last_name = last_name
        self.relationship = relationship
        self.status =status
        self.work = work

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
    
    def __init__(self, name):
        
        self.username = None
        self.password = None
    
    def create_user(self, username, password):
        
        print ("Creating user...")
        self.username =input("Enter username: " )
        self.password=input("Enter password: " )
        print ("created user...")

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

    def check_login(self,username, password): 
        print ("Checking login...")
        check_3=input("Please enter your username: ")
        check_2=input("Please enter your passwork: ")
        if check_3==self.username and check_2==self.password:
            print ("Checking password...")
            print("WELLCOME Mr "+ self.name)
            return True
        elif check_3!=self.username:
            print("Your username is incorrect.\n")
        
        elif check_2!=self.password:
            print("Your password is incorrect.\n")

        else:
            if check_3 and check_2=="":
                raise TypeError("Please enter your username and passwork corretly: ")


print("Hello to my address book!\n")


if __name__ == '__main__':
    pass