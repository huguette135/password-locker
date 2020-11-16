
#!/usr/bin/env python3.6

from user import User
from credential import Credential

def create_user(name, password):
    '''
    Function to create a user account
    Args:
        name : the name the user wants for the account
        password : the password the user want for the account
    '''

    new_user = User(name,password)

    return new_user
