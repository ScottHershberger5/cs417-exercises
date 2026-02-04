def validate_password(password):
    if type(password) != str:
        raise TypeError("password is not a string")
    
    lower_password = password.lower()
    if lower_password != password:
        if any(char.isdigit() for char in password): # I like this way of checking if a str has a num in it
            # makes a list of bools by iterating throuhg the str password and using .isdigit on all the letters
            return True
    return False
