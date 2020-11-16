from random import choice
import string
# from user import User

'''
Credential class : for creating a credentials for a user
'''

class Credential:
    '''
    Class that generates instances of a users credentials
    '''
     # Empty list of credentials
    credential_list = []

    def __init__(self, user_password, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        Args:
            user_password : password of the user
            credential_name : name of an account
            credential_password : password for the account
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password
def save_credential(self):
'''
Method that saves a user's credentials to credential list
'''
Credential.credential_list.append(self)
@classmethod
    def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        # Length of the generated password
        size = 8
        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password
        @classmethod
    def display_credential(cls,password):
        '''
        Method that returns the credential list
        Args:
            password : the user password
        '''
        user_credential_list = []

        for credential in cls.credential_list:
            if credential.user_password == password:
                user_credential_list.append(credential)

        return user_credential_list
    def delete_credential(self):
        '''
        Method that deletes a user's credentials from credential list
        '''
        Credential.credential_list.remove(self)
    @classmethod
    def find_by_name(cls, name):
        
        '''
        Method that takes in an account name and returns its credentials.
        
        Args:
            account: account name to search for 
            
        Returns:
            credentials of an account name that matches the search .
            
        '''
        
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return credential

