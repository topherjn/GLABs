class UserProfile:
    # use dunders to make private
    # use mutators to initialize them 
    # once we have created them
    def __init__(self,username, email, password) -> None:
        self.__username = username
        self.__email = email
        self.__password = password

    # mutators
    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    # accessors
    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
if __name__ == "__main__":
    profile = UserProfile("nicholson", "nicholsonc@gamil.com", "password")

    print(profile.get_username())
    

    
   
