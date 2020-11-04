import random
number = random.randint(1,100)
user_input = None
i = 0
while user_input != number:
    try:
        user_convert_value = int(user_input)
        if user_convert_value > number:
            print("Меньше")
        elif user_convert_value < number:
            print("Больше")
        else:
            print("Вы угадали число!")
            break
        user_input = input("Введите число! ")
    except:
        if user_input == 'q':
            break


