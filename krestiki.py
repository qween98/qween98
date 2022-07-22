import tkinter as tk
import tkinter.messagebox as tkm
window = tk.Tk()
window.title("крестики нолики")
window.geometry("300x300")
window.resizable(False, False)
area = []
turn = 1
char = ""
def push(button):
    global turn  
    print(turn)
    if turn % 2 == 0:
        char = "O"
    else:
        char = "X"
    if  button["text"] == "":
        button["text"] = char
        if char == "X":
            button["bg"] = "aqua"
        else:
            button["bg"] = "yellow"
        turn += 1   
        if check_winner() == "X":
            print("Победили X")
            tkm.showinfo(title = "Победа", message = "Победили X")
            new_game()
        if check_winner() == "O":
            print("Победили O")
            tkm.showinfo(title = "Победа", message = "Победили O")
            new_game()
        if check_winner() == "*" and turn == 10:
            print("Ничья")
            tkm.showinfo(title = "Конец игры", message = "Ничья")
            new_game()    
for x in range(3):
    area.append([])
    for y in range(3):
        button = tk.Button(window, text = "", width = 13, height = 6)
        area[x].append(button)
        area[x][y].place(x = x*100, y = y*100)
        area[x][y]["command"] = lambda selectet_button = button: push(selectet_button)
        area[x][y]["bg"] = "wheat"


def check_winner():
    if area[0][0]["text"] == "X" and area[0][1]["text"] == "X" and area[0][2]["text"] == "X":
        return "X"
    if area[1][0]["text"] == "X" and area[1][1]["text"] == "X" and area[1][2]["text"] == "X":
        return "X"
    if area[2][0]["text"] == "X" and area[2][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][0]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][1]["text"] == "X" and area[1][1]["text"] == "X" and area[2][1]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][2]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "X" and area[1][1]["text"] == "X" and area[2][2]["text"] == "X":
        return "X"
    if area[0][2]["text"] == "X" and area[1][1]["text"] == "X" and area[2][0]["text"] == "X":
        return "X"
    if area[0][0]["text"] == "O" and area[0][1]["text"] == "O" and area[0][2]["text"] == "O":
        return "O"
    if area[1][0]["text"] == "O" and area[1][1]["text"] == "O" and area[1][2]["text"] == "O":
        return "O"
    if area[2][0]["text"] == "O" and area[2][1]["text"] == "O" and area[2][2]["text"] == "O":
        return "O"
    if area[0][0]["text"] == "O" and area[1][0]["text"] == "O" and area[2][0]["text"] == "O":
        return "O"
    if area[0][1]["text"] == "O" and area[1][1]["text"] == "O" and area[2][1]["text"] == "O":
        return "O"
    if area[0][2]["text"] == "O" and area[1][2]["text"] == "O" and area[2][2]["text"] == "O":
        return "O"
    if area[0][0]["text"] == "O" and area[1][1]["text"] == "O" and area[2][2]["text"] == "O":
        return "O"
    if area[0][2]["text"] == "O" and area[1][1]["text"] == "O" and area[2][0]["text"] == "O":
        return "O"
    return "*"


def new_game():
    global area, turn
    turn = 1
    for x in range(3):
        for y in range(3):
            area[x][y]["text"] = ""
            area[x][y]["bg"] = "wheat"

    

            

        
    




window.mainloop()

