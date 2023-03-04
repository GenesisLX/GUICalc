import tkinter as tk
# from gui import App

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()


def add_example(arg):
    input_example.insert(tk.END, arg)

def make_button(arg):
    return tk.Button(text=arg, command=lambda: add_example(arg))

def make_button_history(example, arg):
    return tk.Button(text=f"{example} = {arg}", command=lambda: add_example(arg))

calculation_result = []


def add_to_list(example, result):
    calculation_result.insert(0, {"example": example, "result": result})
    for i, item in enumerate(calculation_result):
        make_button_history(item["example"], item["result"]).grid(row=i+1, column=4, stick="wens")
    if len(calculation_result) == 6:
        del calculation_result[5]



def calculate(event=None):
    example = input_example.get()
    input_example.delete(0, tk.END)
    try:
        result = eval(example)
    except Exception as e:
        input_example.insert(0, str(e))
    else:
        input_example.insert(0, result)
        add_to_list(example, result)



def add_example_pm():
    last_symbol = 0
    examination = "+-/*%"
    example = input_example.get()

    for i in range(len(example)):
        if example[i] in examination:
            last_symbol = i
    if last_symbol != 0:
        input_example.insert(last_symbol + 1, "-")
    else:
        input_example.insert(0, "-")


def add_example_square():
    input_example.insert(tk.END, "**2")

def add_example_PI():
    input_example.insert(tk.END, "3.1415")

def add_example_delete_symbol():
    input_example.delete(len(input_example.get())-1, tk.END)

def add_example_delete():
    input_example.delete(0, tk.END)



window = tk.Tk()
input_example = tk.Entry(width=35, master=window)
input_example.grid(column=0, row=0, columnspan=4, stick="wens")
text = tk.Label(text="Журнал").grid(column=4, row=0, stick="wens")


#Создаём первую строчку в калькуляторе

make_button("/").grid(row=1, column=0, stick="wens")
tk.Button(text="x²", command=add_example_square).grid(row=1, column=1, stick="wens")
tk.Button(text="P", command=add_example_PI).grid(row=1, column=2, stick="wens")
tk.Button(text="del", command=add_example_delete_symbol).grid(row=1, column=3, stick="wens")

#Создаём вторую строчку в калькуляторе
make_button("**").grid(row=2, column=0, stick="wens")
make_button("//").grid(row=2, column=1, stick="wens")
make_button("%").grid(row=2, column=2, stick="wens")
tk.Button(text="CE", command=add_example_delete).grid(row=2, column=3, stick="wens")

#Создаём третью строчку в калькуляторе
make_button("7").grid(row=3, column=0, stick="wens")
make_button("8").grid(row=3, column=1, stick="wens")
make_button("9").grid(row=3, column=2, stick="wens")
make_button("*").grid(row=3, column=3, stick="wens")



#Создаём чётвёртую строчку в калькуляторе
make_button("4").grid(row=4, column=0, stick="wens")
make_button("5").grid(row=4, column=1, stick="wens")
make_button("6").grid(row=4, column=2, stick="wens")
make_button("-").grid(row=4, column=3, stick="wens")

#Создаём пятую строчку
make_button("1").grid(row=5, column=0, stick="wens")
make_button("2").grid(row=5, column=1, stick="wens")
make_button("3").grid(row=5, column=2, stick="wens")
make_button("+").grid(row=5, column=3, stick="wens")


#Создаём шестую строчку
tk.Button(text="+/-", command=add_example_pm).grid(row=6, column=0, stick="wens")
make_button("0").grid(row=6, column=1, stick="wens")
make_button(".").grid(row=6, column=2, stick="wens")
tk.Button(text="=", command=calculate).grid(row=6, column=3, stick="wens")


for i in range(7):
    if i < 4:
        window.columnconfigure(i, weight=1, minsize=75)
        window.grid_columnconfigure(i, minsize=55)
    window.rowconfigure(i, weight=1, minsize=50)
    window.grid_rowconfigure(i, minsize=50)



window.bind("<Return>", lambda event: calculate(event))

for i in range(10):
    window.bind(str(i), lambda event, x=i: add_example(x))

window.mainloop()
