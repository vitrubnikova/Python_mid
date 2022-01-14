import tkinter as tk
root = tk.Tk()
root_2 = tk.Tk()

root.title("First Window")
root_2.title("New Window")
root.geometry("600x400+500+200")
root.iconbitmap("iconsmind-outline-code-window.ico") #расширение обязательно .ico, цвет ЧБ
root.resizable(False, False)
label_1 = tk.Label(master=root, font=('Arial', 20, 'bold'), #объект этикетка, Ctrl + наведение на объект + ЛКМ - для инфо
                   text="Hello\nThere!", bg='red', fg='yellow',
                   width=10,
                   height=3,
                   padx=85, #px
                   pady=50, #px
                   anchor='n', #передается первая буква названия стороны света, по дефолту - значение center
                   relief=tk.RAISED, #варианты: SUNKEN, FLAT, RIDGE, GROOVE, SOLID (можно передавать строкой, в кавычках)
                   bd=20, #px
                   justify='left'
                   )
label_1.pack() #команда для размещения в окне
root.mainloop() #весь код пишется до этого метода
root_2.mainloop()
