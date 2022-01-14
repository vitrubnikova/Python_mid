import tkinter as tk
from tkinter import Button

bomb = 100  # таймер
score = 0  # счет
press_return = True  # начало/конец игры

# окно для игры
root = tk.Tk()
root.title("Game")
root.geometry("600x600+500+400")
root.iconbitmap("discord-16.ico")

# надписи
label = tk.Label(root, text='Жми [enter] для начала игры', font=('Comic Sans MS', 12))
label.pack()
fuse_label = tk.Label(root, text=f'Таймер: {str(bomb)}', font=('Comic Sans MS', 14))
fuse_label.pack()
score_label = tk.Label(root, text=f'Счет: {str(score)}', font=('Comic Sans MS', 14))
score_label.pack()

# объекты PhotoImage
img_1 = tk.PhotoImage(file="1.png")
img_2 = tk.PhotoImage(file="2.png")
img_3 = tk.PhotoImage(file="3.png")
img_4 = tk.PhotoImage(file="4.png")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()


def update_display():  # помещает новые данные в окно
    global bomb
    global score
    if bomb >= 80:
        bomb_label.config(image=img_1)
    elif 50 <= bomb < 80:
        bomb_label.config(image=img_2)
    elif 0 < bomb < 50:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)
    fuse_label.config(text='Таймер: ' + str(bomb))
    score_label.config(text='Счет: ' + str(score))
    fuse_label.after(100, update_display)


def is_alive():  # проверяет, не закончилась ли игра, если значение переменной bomb > 0 - должно возвращаться True
    global bomb
    global press_return
    if bomb <= 0:
        bomb = 0  # для вида
        label.config(text='Bang! Bang! Bang!')  # надпись
        press_return = True
        return False
    else:
        return True


def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)  # длина промежутков времени, милисек


def update_score():
    global score
    if is_alive():
        score += 1
        score_label.after(3000, update_score)


def start(event):
    global press_return  # проверка статуса переменной
    if not press_return:
        pass
    else:
        update_bomb()
        update_score()
        update_display()
        label.config(text='')  # убирает надпись про нажатие кнопки Enter
        press_return = False  # значит запущена игра


def click():
    global bomb
    if is_alive():
        bomb += 1


click_button: Button = tk.Button(root, text='Click me',
                                 bg='black', fg='white',
                                 width=15, font=('Comic Sans MS', 14), command=click,
                                 )
click_button.pack()

root.bind('<Return>', start)
root.mainloop()
