print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    f_num = input("\nFirst num: ")
    if f_num == 'q':
        break
    s_num = input("\nSecond num: ")
    if s_num == 'q':
        break
    try:
        ans = int(f_num) / int(s_num)
    except ZeroDivisionError:
        print("u cant div on 0")
    else:
        print(ans)

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print('Sorry ur file doesnt exist')
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['AliceInW','Essentials','Doesnt exist']
for filename in filenames:
    count_words(filename)
