from tkinter import *

# from PIL import Image, ImageTK
# import random

window = Tk()
window.title("Online game")
window.minsize(width=500, height=500)
window.resizable(width=False, height=False)

label = Label(text="圈圈叉叉", font=("標楷體", 20, "bold"), width=8, height=1, padx=5, pady=5, bg="black", fg="white")
label.place(relx=0.5, rely=0.25, anchor="center")

def reset_interface():
    for widget in window.winfo_children():
        widget.destroy()
    instruction()

def instruction():
    label = Label(text="進階版遊戲說明：\n遊戲中每位玩家只能在棋盤上擁有3個符號，當玩家點擊放置第4個符號時，最早放置的符號將會自動消失，保持棋盤上最多3個符號。\n此遊戲可以增加玩家的策略思考以及記憶力，並跳脫傳統圈圈叉叉的特性，增加遊戲時長，也讓玩家在一次次不同的局勢下，創造出更加刺激的比賽。", font=("標楷體", 16, "bold"), padx=5, pady=5, fg="black", justify="left",  wraplength=400)
    label.place(relx=0.5, rely=0.5, anchor="center")

    button = Button(text="?", font=("標楷體", 14, "bold"), width=1, height=1, padx=5, pady=5, fg="black",
                    command=reset_game_interface)
    button.place(relx=0.9, rely=0.9, anchor="center")

def reset_game_interface():
    for widget in window.winfo_children():
        widget.destroy()
    create_initial_interface()

def create_initial_interface():
    label = Label(window, text="圈圈叉叉", font=("標楷體", 20, "bold"), width=8, height=1, padx=5, pady=5, bg="black", fg="white")
    label.place(relx=0.5, rely=0.25, anchor="center")

    button = Button(window, text="正常版", font=("標楷體", 14, "bold"), padx=5, pady=5, bg="black", fg="white", command=button_clicked)
    button.place(relx=0.25, rely=0.5, anchor="center")

    button = Button(window, text="進階版", font=("標楷體", 14, "bold"), padx=5, pady=5, bg="black", fg="white", command=button_clicked_1)
    button.place(relx=0.75, rely=0.5, anchor="center")

    button = Button(text="?", font=("標楷體", 14, "bold"), width=1, height=1, padx=5, pady=5, fg="black",
                    command=reset_interface)
    button.place(relx=0.9, rely=0.9, anchor="center")

#正常版
players = ["o", "x"]
i = 0

def check():
    space = 9
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != " ":
            buttons[row][0].config(bg="lime")
            buttons[row][1].config(bg="lime")
            buttons[row][2].config(bg="lime")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != " ":
            buttons[0][column].config(bg="lime")
            buttons[1][column].config(bg="lime")
            buttons[2][column].config(bg="lime")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        buttons[0][0].config(bg="lime")
        buttons[1][1].config(bg="lime")
        buttons[2][2].config(bg="lime")
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        buttons[0][2].config(bg="lime")
        buttons[1][1].config(bg="lime")
        buttons[2][0].config(bg="lime")
        return True
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != (" " or "  "):
                space -= 1
    if space == 0:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return True

def game(row, column):
    global i
    if buttons[row][column]["text"] == " ":
        buttons[row][column]["text"] = players[i]
        i += 1
        if (i >= 2):
            i -= 2
    if check() is True:
        for row in range(3):
            for column in range(3):
                if buttons[row][column]["text"] == " ":
                    buttons[row][column]["text"] = "  "

def restart_clicked():
    for row in range(3):
        for column in range(3):
            buttons[row][column]["text"] = " "
            buttons[row][column].config(bg="#F0F0F0")

def button_clicked():
    global buttons
    canvas = Canvas(window, width=600, height=600)
    canvas.pack()
    canvas.create_line(120, 240, 480, 240, width=5)
    canvas.create_line(120, 360, 480, 360, width=5)
    canvas.create_line(240, 120, 240, 480, width=5)
    canvas.create_line(360, 120, 360, 480, width=5)
    restart = Button(text="restart", font=("Arial", 14, "bold"), padx=5, pady=5, fg="black",
                     command=lambda: restart_clicked())
    canvas.create_window(300, 60, window=restart)

    back = Button(window, text="back", font=("Arial", 12), padx=5, pady=5, command=reset_game_interface)
    back.place(relx=0.1, rely=0.07)

    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(text=" ", font=("標楷體", 16), width=10, height=5,
                                          command=lambda row=row, column=column: game(row, column))
            buttons[row][column].pack
            canvas.create_window(180 + column * 120, 180 + row * 120, window=buttons[row][column])

# 進階版
players_1 = ["o", "x"]
i_1 = 0

def check_1():
    for row_1 in range(3):
        if buttons_1[row_1][0]["text"] == buttons_1[row_1][1]["text"] == buttons_1[row_1][2]["text"] != " ":
            buttons_1[row_1][0].config(bg="lime")
            buttons_1[row_1][1].config(bg="lime")
            buttons_1[row_1][2].config(bg="lime")
            return True
    for column_1 in range(3):
        if buttons_1[0][column_1]["text"] == buttons_1[1][column_1]["text"] == buttons_1[2][column_1]["text"] != " ":
            buttons_1[0][column_1].config(bg="lime")
            buttons_1[1][column_1].config(bg="lime")
            buttons_1[2][column_1].config(bg="lime")
            return True
    if buttons_1[0][0]["text"] == buttons_1[1][1]["text"] == buttons_1[2][2]["text"] != " ":
        buttons_1[0][0].config(bg="lime")
        buttons_1[1][1].config(bg="lime")
        buttons_1[2][2].config(bg="lime")
        return True
    if buttons_1[0][2]["text"] == buttons_1[1][1]["text"] == buttons_1[2][0]["text"] != " ":
        buttons_1[0][2].config(bg="lime")
        buttons_1[1][1].config(bg="lime")
        buttons_1[2][0].config(bg="lime")
        return True

def game_1(row_1, column_1):
    global i_1, record_1
    if buttons_1[row_1][column_1]["text"] == " ":
        buttons_1[row_1][column_1]["text"] = players_1[i_1]
        record_1.append((row_1, column_1))  # 記錄新的一步

        if len(record_1) > 6:
            r, c = record_1.pop(0)
            buttons_1[r][c]["text"] = " "

        i_1 += 1
        if (i_1 >= 2):
            i_1 -= 2
    if check_1() is True:
        for row_1 in range(3):
            for column_1 in range(3):
                if buttons_1[row_1][column_1]["text"] == " ":
                    buttons_1[row_1][column_1]["text"] = "  "

def restart_clicked_1():
    global record_1
    for row_1 in range(3):
        for column_1 in range(3):
            buttons_1[row_1][column_1]["text"] = " "
            buttons_1[row_1][column_1].config(bg="#F0F0F0")
            record_1 = []

def button_clicked_1():
    global buttons_1, record_1
    canvas_1 = Canvas(window, width=600, height=600)
    canvas_1.pack()
    canvas_1.create_line(120, 240, 480, 240, width=5)
    canvas_1.create_line(120, 360, 480, 360, width=5)
    canvas_1.create_line(240, 120, 240, 480, width=5)
    canvas_1.create_line(360, 120, 360, 480, width=5)
    restart_1 = Button(text="restart", font=("Arial", 14, "bold"), padx=5, pady=5, fg="black",
                       command=lambda: restart_clicked_1())
    canvas_1.create_window(300, 60, window=restart_1)

    back_1 = Button(window, text="back", font=("Arial", 12), padx=5, pady=5, command=reset_game_interface)
    back_1.place(relx=0.1, rely=0.07)

    buttons_1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    record_1 = []  # 紀錄順序

    for row_1 in range(3):
        for column_1 in range(3):
            buttons_1[row_1][column_1] = Button(text=" ", font=("標楷體", 16), width=10, height=5,
                                                command=lambda row_1=row_1, column_1=column_1: game_1(row_1, column_1))
            buttons_1[row_1][column_1].pack  # (row=row, column=column)
            canvas_1.create_window(180 + column_1 * 120, 180 + row_1 * 120, window=buttons_1[row_1][column_1])


button = Button(text="正常版", font=("標楷體", 14, "bold"), padx=5, pady=5, bg="black", fg="white",
                command=button_clicked)
button.place(relx=0.25, rely=0.5, anchor="center")

button = Button(text="進階版", font=("標楷體", 14, "bold"), padx=5, pady=5, bg="black", fg="white",
                command=button_clicked_1)
button.place(relx=0.75, rely=0.5, anchor="center")

button = Button(text="?", font=("標楷體", 14, "bold"), width=1, height=1, padx=5, pady=5, fg="black",
                command=reset_interface)
button.place(relx=0.9, rely=0.9, anchor="center")


window.mainloop()