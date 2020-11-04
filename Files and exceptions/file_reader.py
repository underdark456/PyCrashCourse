#To do any work with a file need to open the file to access it
#open() function returns an object representing the file
#"with" closes the file once access to it is no longer needed
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string='' #hold the digits of pi
# for line in lines:
#     pi_string +=line.strip() #adds each line of digits to pi_string, remove whitespaces
# print(pi_string)
# print(len(pi_string))

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string +=line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter ur birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your bday in PI!!")
else:
    print("Ты обосрался и твоего др нет в числе Pi")