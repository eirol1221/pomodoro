from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

reps = 0
checks = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global reps, checks
    reps = 0
    checks = ""
    lbl_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    count = 0
    reps += 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        lbl_timer.config(text="WORK")
        count = WORK_MIN
    elif reps == 2 or reps == 4 or reps == 6:
        lbl_timer.config(text="BREAK", fg=PINK)
        count = SHORT_BREAK_MIN
    elif reps == 8:
        lbl_timer.config(text="BREAK", fg=RED)
        count = LONG_BREAK_MIN

    count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(min_count, sec_count=0):
    global checks, reps
    print(type(min_count))

    if sec_count < 10:
        canvas.itemconfig(timer_text, text=f"{min_count}:0{sec_count}")
    else:
        canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")

    if min_count >= 0 and sec_count > 0:
        window.after(100, count_down, min_count, sec_count - 1)
    elif min_count == 0 and sec_count == 0:
        canvas.itemconfig(timer_text, text=f"{min_count}:0{sec_count}")
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            checks += "✔"
            lbl_check.config(text=checks)
        start_timer()
    elif sec_count == 0:
        window.after(100, count_down, min_count - 1, sec_count + 59)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Buttons
btn_start = Button(text="Start", font=("Arial", 10, "bold"), bg="white", highlightthickness=0, command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", font=("Arial", 10, "bold"), bg="white", highlightthickness=0, command=reset_time)
btn_reset.grid(row=2, column=2)

# Labels
lbl_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
lbl_timer.grid(row=0, column=1)

lbl_check = Label(text="", font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
lbl_check.grid(row=3, column=1)


window.mainloop()