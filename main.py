from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_second = WORK_MIN * 60
    short_brake_second = SHORT_BREAK_MIN * 60
    long_brake_second = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_brake_second)
        title_label.config(text="break", fg=RED)
    if reps % 2 == 0:
        count_down(short_brake_second)
        title_label.config(text="break", fg=PINK)
    else:
        count_down(work_second)
        title_label.config(text="working", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count > 0:
        print(count)
        window.after(1000, count_down, count - 1)  # built in method that calls count-down method every second to
                                                   # refresh the gui
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)  # bg:- background color




title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # to create a photo image data
canvas.create_image(100, 112, image=tomato_img)  # place the image at the specific location and put the image inside
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # to right a text in the canva
canvas.grid(column=1, row=1)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

restart_button = Button(text="restart", highlightthickness=0)
restart_button.grid(column=2, row=2)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
