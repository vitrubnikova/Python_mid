import random

# создание списков
l_of_q = [
    "Ты когда-нибудь занимался читерством?",
    "Умеешь снимать носки пальцами ног?",
    ...
]  # вопросы
l_of_a = [
    "Расскажи смешную шутку",
    "Обними кого-нибудь/что-нибудь",
    "Отправь кому-нибудь сообщение или напиши код носом",
    ...
]  # действия
gamer_l = []  # игроки


#  ФУНКЦИИ
def gamers(list):  # для добавления игроков
    while True:  # цикл
        name = input("Имя игрока: ")  # принимает введенное значение
        list.append(str.capitalize(name))  # в список добавляется значение переменной
        # защита от "дурака"
        if 0 < len(name) <= 2:  # проверка, если игроков 2 или меньше
            continue  # цикл продолжается
        # условия
        if len(list) >= 2:  # если длина списка больше 2
            need_next_player = input("Нужно больше игроков? - д/н ")  # будет ли еще один игрок
            if need_next_player == str.lower("д") or need_next_player == str.lower("да"):  # если пользователь соглашается
                continue  # продолжается
            else:
                break  # прерывание


gamers(gamer_l)  # вызов функции


def game(l_of_q, l_of_a, *args):  # логика игры
    while True:
        next_step = None
        for gamer in args:  # цикл для каждого игрока в списке
            print(gamer)  # вывод игрока
            user_choise = input("Правда или действие? ")  # принимается значение выбора игрока
            if user_choise == str.lower("в") or user_choise == str.lower("вопрос"):  # если пользователь выбирает ВОПРОС
                q_index = random.randint(0, len(l_of_q)-1)  # рандомно выбирается индекс элемента из списка вопросов
                print(l_of_q[q_index])  # вывод вопроса с помощью обращения к нему по индексу списка
                l_of_q.pop(q_index)
            elif user_choise == str.lower("д") or user_choise == str.lower("действие"):  # если пользователь выбирает ДЕЙСТВИЕ
                a_index = random.randint(0, len(l_of_a)-1)  # рандомно выбирается индекс элемента из списка действий
                print(l_of_a[a_index])  # вывод действия с помощью обращения к нему по индексу списка
                l_of_q.pop(a_index)
            else:
                print("Делай или отвечай")
                q_index = random.randint(0, len(l_of_q) - 1)  # рандомно выбирается индекс элемента из списка вопросов
                print(l_of_q[q_index])  # вывод вопроса с помощью обращения к нему по индексу списка
                l_of_q.pop(q_index)
                a_index = random.randint(0, len(l_of_a) - 1)  # рандомно выбирается индекс элемента из списка действий
                print(l_of_a[a_index])  # вывод действия с помощью обращения к нему по индексу списка
                l_of_q.pop(a_index)
            # условие выхода из цикла игры
            if args[-1] == gamer:
                break
            next_step = input("Следующий игрок? - д/н ")
            if next_step == str.lower("д") or next_step == str.lower("да"):
                continue
            else:
                print("GAME OVER")
                break
        if next_step == str.lower('д') or next_step == str.lower("да"):
            pass
        else:
            break
        select = input("Новый раунд? - д/н ")
        if select == str.lower("д") or select == str.lower("да"):
            continue
        else:
            break


game(l_of_q, l_of_a, *gamer_l)  # вызов функции