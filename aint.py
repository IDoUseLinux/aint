import tkinter as tk
from tkinter import messagebox 
from random import SystemRandom ## Lets make this truely random!

## (C) IDoUseLinux, MIT License, 2023

def spoof_text(ai_text, scramble_aggresiveness) :
    spoofed_text = ''
    for letter in ai_text :
        ## We take the original string and start scrambling it with look-alikes
        if letter == "a" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "а"
        elif letter == "c" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "с"
        elif letter == "d" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ԁ"
        elif letter == "h" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "һ"
        elif letter == "i" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "і"
        elif letter == "j" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ј"
        elif letter == "n" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ո"
        elif letter == "o" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = ["о", "ο", "օ" ][SystemRandom().randint(0,2)]
        elif letter == "q" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "р"
        elif letter == "v" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ν"
        elif letter == "x" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "х"
        elif letter == "y" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "у"
        elif letter == ";" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = ";"
        elif letter == "." and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "․"
        elif letter == "," and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "‚"

        ## The invisible characters
        if SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter += "‎"*SystemRandom().randrange(0,5)
        if SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter += "‍"*SystemRandom().randrange(0,5)
        spoofed_text += letter
    return spoofed_text 

class GUI :
    APP_BG_COLOR = "#192e45"
    BAR_COLOR = "#346191"
    ENTRY_COLOR = "#15283c"
    TEXT_COLOR="#ffffff"
    all_screen_obj = []

    def __init__(self, app) :
        self.app = app
        self.app.geometry("600x500")
        self.app.title("Ain't (Ai Ain't)")
        self.app.configure(bg=self.APP_BG_COLOR)
        self.spawn_screen()
        self.app.mainloop()

    def clear_screen(self) :
        while self.all_screen_obj: 
            self.all_screen_obj[0].destroy()
            del self.all_screen_obj[0]

    def spawn_screen(self) :
        frame = tk.Frame(self.app, bg=self.BAR_COLOR, width=600, height=0, padx=0, pady=0)
        frame.pack(padx=0, pady=0, fill="both")

        program_name = tk.Label(frame, text="Ain't (Ai Ain't, great name, I know...)", font=("Segoe UI", 20), fg=self.TEXT_COLOR, bg=self.BAR_COLOR)
        program_name.pack(side=tk.TOP, padx=0, pady=(20,20))

        instruction = tk.Label(self.app, text="Enter the AI-tagged text: ", font=("Segoe UI", 20),fg=self.TEXT_COLOR, bg=self.APP_BG_COLOR)
        instruction.pack(side=tk.TOP, pady=10)

        self.text_entry = tk.Text(self.app, bg=self.ENTRY_COLOR, fg=self.TEXT_COLOR, width=200, height=8, font=("Segoe UI", 15), insertbackground="#ffffff", border=5 ) ## For some dumb reason, the height is measured by how many lines it is, not actually how many pixels. 
        self.text_entry.pack(anchor=tk.CENTER, padx=30, pady=30)

        sumbit_button = tk.Button(self.app, bg="red", fg=self.TEXT_COLOR, text="Spoof", command=self.__spoof_text__)
        sumbit_button.pack(side=tk.TOP, pady=10)

        self.all_screen_obj.append(program_name)
        self.all_screen_obj.append(frame)
        self.all_screen_obj.append(self.text_entry)
 
    ## We are going to add the about later.
    def spawn_about(self) :
        pass

    def __spoof_text__(self) :
        text = self.text_entry.get("1.0", tk.END)
        self.text_entry.delete("1.0", tk.END)
        self.text_entry.insert("1.0", spoof_text(text, scramble_aggresiveness=10))

if __name__ == "__main__" : 
    ## Tkinter genuinely sucks
    ## CustomTKinter is much better
    app = tk.Tk()
    GUI(app)
