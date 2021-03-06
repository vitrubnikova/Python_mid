import random


# объявление функций

def game(choice, result):  # choice - выбор пользователя, result - счет
    print("")  # доп вывод для переноса строки
    print("=====Начало игры Камень, Ножницы, Бумага=====")  # вывод на экран названия игры и сообщение о старте
    comp_choice = random.choice("кнб")  # переменная для выбора компа с помощью рандома
    print("--------------------------------")
    print("Ваш выбор: ", str.capitalize(choice))
    print("Выбор бота: ", str.capitalize(comp_choice))
    if str.lower(choice) == comp_choice:  # выбор компа = выбору пользователя
        print("Результат раунда - ничья")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")  # вывод на экран счета
    elif str.lower(choice) == "к" and comp_choice == "б":  # игрок выбирает "камень", а компьютеру выпадает "бумага"
        result["бот"] += 1  # выигрывает компьютер (счет увеличивается на 1 очко)
        print("------Победа бота------")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")
    elif str.lower(choice) == "к" and comp_choice == "н":  # игрок выбирает "камень", а компьютеру выпадает "ножницы"
        result["юзер"] += 1  # счет в пользу игрока (увеличивается на 1 очко)
        print("------Победа юзера------")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")
    elif str.lower(choice) == "б" and comp_choice == "н":  # игрок выбирает "бумагу", а компьютеру выпадает "ножницы"
        result["бот"] += 1  # выигрывает компьютер (счет увеличивается на 1 очко)
        print("------Победа бота------")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")
    elif str.lower(choice) == "б" and comp_choice == "к":  # игрок выбирает "бумагу", а компьютеру выпадает "камень"
        result["юзер"] += 1  # счет в пользу игрока (увеличивается на 1 очко)
        print("------Победа юзера------")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")
    elif str.lower(choice) == "н" and comp_choice == "к":  # игрок выбирает "ножницы", а компьютеру выпадает "камень"
        result["бот"] += 1  # выигрывает компьютер (счет увеличивается на 1 очко)
        print("------Победа бота------")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")
    elif str.lower(choice) == "н" and comp_choice == "б":  # игрок выбирает "ножницы", а компьютеру выпадает "бумага"
        result["юзер"] += 1  # счет в пользу игрока (увеличивается на 1 очко)
        print("------Победа юзера------")
        print("Счет: Бот", result["бот"], "-", result["юзер"], "Игрок")


# входные параметры
start_score = {"бот": 0, "юзер": 0}  # вначале у всех по нулям счет
user_choose = input("Выбор К / Н / Б - ")  # переменная принимает значения

# вызов функции
game(result=start_score, choice=user_choose)
