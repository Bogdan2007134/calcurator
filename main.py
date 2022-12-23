import tkinter as tk

gbvalue = 0
gbvalue2 = 0
movie = ""

def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0,value + str(digit))
    

def alike_digit():
    print(calc.get())
    value = calc.get()
    calc.delete(0, tk.END)
    global gbvalue, gbvalue2, movie
    if gbvalue != 0:
        if movie == "+":
            a = int(gbvalue) + int(value)
            calc.insert(0,a)
            print("4")
        elif movie == "*":
            a = int(gbvalue) * int(value)
            calc.insert(0,a)
        elif movie == "-":
            a = int(gbvalue) - int(value)
            calc.insert(0,a)
        elif movie == "/":
            a = int(gbvalue) / int(value)
            calc.insert(0,a)
    else:
        print("5")


def delete_digit():  # Удаление всех параметров
    global gbvalue, gbvalue2, movie
    gbvalue = 0
    gbvalue2 = 0
    movie = ""
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def math_digit(mov):
    global gbvalue, movie
    value = calc.get()
    if  value[-1] in '-+*/':
        value = value[:-1]
    gbvalue = value
    movie = mov
    calc.insert(0, value + mov)
    calc.delete(0, tk.END)
    calc.insert(0, 0)
    print(gbvalue, mov)



root = tk.Tk()
root.geometry(f"250x400+490+200")
root['bg'] = 'gray1'
root.title("Калькулятор")


calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 19), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we')

tk.Button(text="1", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(1)).grid(row=2, column=0, stick='wens', padx=3, pady=5)
tk.Button(text="2", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(2)).grid(row=2, column=1, stick='wens', padx=3, pady=5)
tk.Button(text="3", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(3)).grid(row=2, column=2, stick='wens', padx=3, pady=5)
tk.Button(text="4", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(4)).grid(row=3, column=0, stick='wens', padx=3, pady=5)
tk.Button(text="5", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(5)).grid(row=3, column=1, stick='wens', padx=3, pady=5)
tk.Button(text="6", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(6)).grid(row=3, column=2, stick='wens', padx=3, pady=5)
tk.Button(text="7", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(7)).grid(row=4, column=0, stick='wens', padx=3, pady=5)
tk.Button(text="8", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(8)).grid(row=4, column=1, stick='wens', padx=3, pady=5)
tk.Button(text="9", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(9)).grid(row=4, column=2, stick='wens', padx=3, pady=5)
tk.Button(text="0", bg= 'gray15', bd=0, fg='White', font=('Arial', 25), command=lambda : add_digit(0)).grid(row=5, column=0,columnspan=3, stick='wens', padx=3, pady=5)
tk.Button(text="/", bg= 'chocolate2', bd=0, font=('Arial', 25), command=lambda : math_digit("/")).grid(row=1, column=3, stick='wens', padx=3, pady=5)
tk.Button(text="*", bg= 'chocolate2', bd=0, font=('Arial', 25), command=lambda : math_digit("*")).grid(row=2, column=3, stick='wens', padx=3, pady=5)
tk.Button(text="-", bg= 'chocolate2', bd=0, font=('Arial', 25), command=lambda : math_digit("-")).grid(row=3, column=3, stick='wens', padx=3, pady=5)
tk.Button(text="+", bg= 'chocolate2', bd=0, font=('Arial', 25), command=lambda : math_digit("+")).grid(row=4, column=3, stick='wens', padx=3, pady=5)
tk.Button(text="=", bg= 'chocolate2', bd=0, font=('Arial', 25), command=lambda : alike_digit()).grid(row=5, column=3, stick='wens', padx=3, pady=5)
tk.Button(text="c", bg= 'gray60', bd=0, font=('Arial', 25), command=lambda : delete_digit()).grid(row=1, column=0, columnspan=3, stick='we', padx=3, pady=5)

root.grid_columnconfigure(0,minsize=60)
root.grid_columnconfigure(1,minsize=60)
root.grid_columnconfigure(2,minsize=60)
root.grid_columnconfigure(3,minsize=70)

root.grid_rowconfigure(1,minsize=60)
root.grid_rowconfigure(2,minsize=60)
root.grid_rowconfigure(3,minsize=60)
root.grid_rowconfigure(4,minsize=60)


root.mainloop()

