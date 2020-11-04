import json
def get_stored_username():
    """This function retrieves a stored username and returns
the username if it finds one. If the file username.json doesn’t exist, the function returns None"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Whats your name?')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

"""call greet_user() -> welcomes back an existing user or greets a new user by calling get_stored_username() or get_new_username()"""