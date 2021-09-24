from tkinter import *
from tkinter import messagebox
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

labels = ['Витамин А', 'Витамин B', 'Витамин C', 'Витамин D', 'Витамин E']
products = ['Яблоко', 'Пшено', 'Говядина', 'Творог', 'Конфеты']
colors = ['coral', 'yellow', 'crimson', 'springgreen', 'darkorange']
vita = np.array([
    [1, 9, 2, 1, 1],
    [10, 1, 2, 1, 1],
    [1, 0, 5, 1, 1],
    [2, 1, 1, 2, 9],
    [2, 1, 2, 13, 2],
])
entries = []
day_norm = np.array([170, 180, 140, 180, 350]).reshape((5, 1))

def check_negative(a):
    for i in a:
        if i < 0:
            return False
        else:
            return True

def clicked():
    for i in range(len(labels)):
        for j in range(len(products)):
            vita[j][i] = int(entries[i][j].get())
    sizes = np.ravel(solve(vita, day_norm))
    if check_negative(sizes):
        # plt.pie(sizes,  labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        # plt.axis('equal')
        # plt.show()

        frameChartsLT = Frame(window)
        frameChartsLT.pack()

        fig = Figure()
        ax = fig.add_subplot(111)
        ax.pie(sizes,  labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()
    else:
        messagebox.showerror('Ошибка', 'Невозможно рассчитать')

window = Tk()
window.title('Жраааат')
window.minsize(width=800, height=600)
app = Frame(window)
app.pack()
c_column = c_row = 0
Label(app, text='Продукты').grid(row=c_row, column=c_column)
c_column = c_column + 1
for i in labels:
    Label(app, text=i).grid(row=c_row, column=c_column)
    c_column = c_column + 1
c_column = 0
c_row = c_row + 1
for pr in products:
    Label(app, text=pr).grid(row=c_row, column=c_column)
    c_column = c_column + 1
    entry_row = []
    for la in range(len(labels)):
        e = Entry(app, width=10)
        e.insert(0, vita[c_column-1][c_row-1])
        e.grid(column=c_column, row=c_row)
        entry_row.append(e)
        c_column = c_column + 1
    entries.append(entry_row)
    c_column = 0
    c_row = c_row + 1
c_column = 0
c_row = c_row + 1
btn = Button(app, text="Рассчитать", command=clicked)
btn.grid(column=c_column, row=c_row)
c_column = c_column + 1
errorLabel = Label(app)
errorLabel.grid(row=c_row, column=c_column)

app.bind('<Escape>', lambda x: app.destroy())
app.mainloop()
