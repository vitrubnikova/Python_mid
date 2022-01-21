import tkinter as tk
import re

# СОЗДАНИЕ ПАТТЕРНОВ

# регулярное выражение для логина
# логин имеет вид: user@domen.com, соотетственно
login_pattern = re.compile(r'^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$')
# r - чтобы служебные символы воспринимались как составная часть строки («сырая» строка называется)
# ^ - означает начало строки
# \w - означает, что вместо него может быть любой буквенно-цифровой символ и нижнее подчеркивание
# {3,20} - минимальное и максимальное количество символов
# @ - потому что логином является e-mail, т.е. обязательно должен быть этот симол
# [a-z] - дапазон буквенных символовлатинского алфавита, которые располагаются после значка "собаки"
# несмотря на «сырую» строку, точка все равно считается служебным символом, поэтому нужно экранировать ее слешем
# $ является симолом окончания строки

# регулярное выражение для пароля
# допустимые символы: буквенно-цифровые и нижнее подчеркивание
# минимальная и максимальная длина пусть будет от восьми до шестнадцати знаков
password_pattern = re.compile(r"^\w{8,16}$")


# ФУНКЦИИ

# при нажатии на клавишу LOGIN
def log_in():
    # получение введенной информации
    login = login_entry.get()
    password = password_entry.get()
    # проверка на соотетсвие паттернам
    if not login_pattern.search(login):
        login_entry.config(bg="red")
        password_entry.config(bg="red")
    else:
        if password_pattern.search(password):  # если все введено ОК
            login_entry.config(bg="green")  # будет подсвечиваться зеленым цетом
            password_entry.config(bg="green")
        else:  # если НЕ ОК
            login_entry.config(bg="red")  # подсвечивается красным цетом
            password_entry.config(bg="red")


# СОЗДАНИЕ И НАСТРОЙКА ОКНА

root = tk.Tk()
root.geometry("400x250+700+500")
root.iconbitmap("1.ico")
root.resizable(False, False)

# надписи, которые будут указывать куда вводить пароль и логин
login_label = tk.Label(
    root,
    text="Login",
    font=("Arial", 14),
    padx=50
)
password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 14),
    padx=50
)

# поля для ввода (используется объект Entry)
login_entry = tk.Entry(
    root,
    font={"Arial", 12},
    width=20
)
password_entry = tk.Entry(
    font=["Arial", 12],
    width=20,
    show="*"  # закрывает пароль от показа
)

# кнопка логина
login_button = tk.Button(
    root,
    text="LOGIN",
    font=("Arial", 16),
    width=12,
    command=log_in
)

# настройка колонок и строк с помощью метода grid
root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)
login_button.grid(columnspan=2)

# размещение элементов в окне
login_label.grid(column=0, row=0,
                 sticky="w")  # sticky работает аналогично атрибуту anchor и выравнивает элементы в соответствии с заданной стороной мира
password_label.grid(column=0, row=1, sticky="w")
login_entry.grid(column=1, row=0, sticky="w")
password_entry.grid(column=1, row=1, sticky="w")
login_button.grid(column=0, row=2)

root.mainloop()
