from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    button1.config(state=ACTIVE)
    button2.config(state=DISABLED)
    global timer_should_continue
    global minutes
    global seconds
    global timer
    global marks
    global iteration_count

    minutes, seconds, timer_should_continue = 2, 0, False
    canvas.itemconfig(timer_text, text=f"0{minutes}:0{seconds}")
    marks = ''

    title.config(text='Timer', fg=GREEN, font=(FONT_NAME, 28))
    chmark.config(text='')

    if timer is not None:
        window.after_cancel(timer)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


minutes, seconds, timer_should_continue = 1, 0, True
#seconds = 0
#timer_should_continue = True
iteration_count = 0
marks = ''


def start_timer():
    global minutes
    global seconds
    global timer_should_continue
    global iteration_count
    timer_should_continue = True
    button1.config(state=DISABLED)
    button2.config(state=ACTIVE)
    global timer

    if timer_should_continue:
        global marks

        tick_count = int(iteration_count//2)

        print(iteration_count)

        if iteration_count == 0:
            marks = ''

        for i in range(0, tick_count):
            print(tick_count)
            if len(marks) < tick_count:
                marks += '🗸'
        chmark.config(text=marks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28))

        if iteration_count % 2 == 0:
            title.config(text='Work', fg=GREEN, font=(FONT_NAME, 28))
        else:
            title.config(text='Break', fg=PINK, font=(FONT_NAME, 28))

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
                iteration_count += 1
                if iteration_count % 2 == 0:
                    minutes = 1
                    if iteration_count == 10:
                        timer_should_continue = False
                        button1.config(state=ACTIVE)
                        button2.config(state=DISABLED)
                        canvas.itemconfig(timer_text, text=f"0{minutes}:0{seconds}")
                        title.config(text='Timer', fg=GREEN, font=(FONT_NAME, 28))

                        if timer is not None:
                            window.after_cancel(timer)
                else:
                    minutes = SHORT_BREAK_MIN - 3
                # timer_should_continue = False
                # button1.config(state=ACTIVE)
                # button2.config(state=DISABLED)
            else:
                seconds = 59
                minutes -= 1
        else:
            seconds -= 1

        timer = window.after(1000, start_timer)


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

chmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
chmark.grid(column=2, row=3)

button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=3, row=3)
button2.config(state=DISABLED)

window.mainloop()
