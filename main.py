from tkinter import *
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    button1.config(state=ACTIVE)
    button2.config(state=DISABLED)
    global timer_should_continue
    global minutes
    global seconds
    minutes = 2
    seconds = 0
    timer_should_continue = False
    canvas.itemconfig(timer_text, text=f"0{minutes}:0{seconds}")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


minutes = 2
seconds = 0
timer_should_continue = True


def start_timer():
    global minutes
    global seconds
    global timer_should_continue
    timer_should_continue = True
    button1.config(state=DISABLED)
    button2.config(state=ACTIVE)

    if timer_should_continue:
        if seconds < 10:
            if minutes < 10:
                canvas.itemconfig(timer_text, text=f"0{minutes}:0{seconds}")
            else:
                canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
        else:
            if minutes < 10:
                canvas.itemconfig(timer_text, text=f"0{minutes}:{seconds}")
            else:
                canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

        if seconds == 0:
            if minutes == 0:
                timer_should_continue = False
                button1.config(state=ACTIVE)
                button2.config(state=DISABLED)
            else:
                seconds = 59
                minutes -= 1
        else:
            seconds -= 1

        window.after(1000, start_timer)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro app")
window.config(padx=50, pady=100)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 28))
title.grid(column=2, row=1)

canvas = Canvas(width=300, height=300, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=2, row=2)

button1 = Button(text="Start", command=start_timer)
button1.grid(column=1, row=3)

button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=3, row=3)
button2.config(state=DISABLED)

window.mainloop()
