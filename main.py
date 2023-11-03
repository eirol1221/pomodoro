from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
TOMATO = "#F05D40"
CINNABAR = "#EF4C38"
GREEN = "#328F43"
YELLOW = "#FFF8C9"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, checks, timer

    btn_start.config(state=NORMAL)
    btn_reset.config(state=DISABLED)

    window.after_cancel(timer)
    reps = 0
    checks = ""
    lbl_check.config(text=checks)
    lbl_timer.config(text="Pomodoro Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    print(reps)
    if reps == 8:
        window.after_cancel(timer)
        return

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    count = 0
    reps += 1

    btn_start.config(state=DISABLED)
    btn_reset.config(state=NORMAL)

    if reps % 2 == 1:
        text = "Time to Work 💪"
        fg = GREEN
        count = WORK_MIN
    elif reps == 8:
        text = "Long Break 😴"
        fg = CINNABAR
        count = LONG_BREAK_MIN
    elif reps % 2 == 0:
        text = "Short Break ☕"
        fg = TOMATO
        count = SHORT_BREAK_MIN

    lbl_timer.config(text=text, fg=fg)
    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(min_count, sec_count=0):
    global checks, reps, timer

    if sec_count < 10:
        canvas.itemconfig(timer_text, text=f"{min_count}:0{sec_count}")
    else:
        canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")

    if min_count >= 0 and sec_count > 0:
        timer = window.after(1000, count_down, min_count, sec_count - 1)
    elif min_count > 0 and sec_count == 0:
        timer = window.after(1000, count_down, min_count - 1, sec_count + 59)
    else:
        canvas.itemconfig(timer_text, text=f"{min_count}:0{sec_count}")
        if reps % 2 == 1:
            checks += "🍅"
            lbl_check.config(text=checks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=30, bg=YELLOW)

canvas = Canvas(width=350, height=350, bg=YELLOW, highlightthickness=0, borderwidth=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(175, 175, image=tomato)
timer_text = canvas.create_text(175, 220, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=0, rowspan=2, ipadx=20, sticky="ew")

# Buttons
start_img = PhotoImage(file="btn-start.png")
btn_start = Button(image=start_img, bg=YELLOW, highlightthickness=0, borderwidth=0, command=start_timer,
                   activebackground=YELLOW)
btn_start.grid(row=1, column=1, sticky='s')

reset_img = PhotoImage(file="btn-reset.png")
btn_reset = Button(image=reset_img, bg=YELLOW, highlightthickness=0, borderwidth=0, command=reset_timer, state=DISABLED,
                   activebackground=YELLOW)
btn_reset.grid(row=2, column=1, sticky='ns')

# pause_img = PhotoImage(file="btn-pause.png")
# btn_pause = Button(image=pause_img, bg=YELLOW, highlightthickness=0, borderwidth=0, command=pause_timer, state=DISABLED)
# btn_pause.grid(row=3, column=1, sticky='e', ipady=0)

# Labels
lbl_timer = Label(text="Pomodoro Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
lbl_timer.grid(row=0, column=0, columnspan=2, sticky='ew')

lbl_check = Label(font=(FONT_NAME, 16, "bold"), fg=TOMATO, bg=YELLOW, pady=20)
lbl_check.grid(row=3, column=0, sticky="ew")

window.mainloop()