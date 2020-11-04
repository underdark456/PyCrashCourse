import json

# filename = 'numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)
# print(numbers)
username = input("Whats ur name? \n")
filename = 'username.json'
with open(filename,'a') as f:
    json.dump(username,f)
    print(f"We'll remeber you when you come back, {username}")