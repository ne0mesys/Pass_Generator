#!/usr/bin/env python3

from customtkinter import *
import signal
import random
import sys

# Colors
red = "\033[1;31m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
green = "\033[1;32m"
nc = "\033[1;37m"  # Reset color

# Quitting from terminal
def def_handler(sig, frame):
    print(f"\n{red}[!] Terminating program...")
    sys.exit(1)


def generate(entry, frame, label3, label4, char, char_special, root, switch):
    try:
        label4.forget()
        label3.forget()
        digits = int(entry.get())
        value = switch.get()
        length = digits 
      
        if length > 40: 
            label3.configure(text=f"Error, the limit is up to 40\n characters!", text_color="red", font=("Arial", 20))
            label3.pack(pady=10, padx=10)
            return

        password = ""
        if value == 0:
            for i in range(length): 
                password += random.choice(char)       
        
        else: 
            for i in range(length):
                password += random.choice(char_special)

        
        label3.configure(frame, text="Your password is: ", text_color="white", font=("Arial", 18))
        label3.pack(pady=10, padx=10)

        label4.configure(text=f"{password}")
        label4.pack(pady=10, padx=10)

        def copy_to_clipboard(event):
            root.clipboard_clear()
            root.clipboard_append(password)
            label4.configure(text="Copied!", text_color="#5bff8f")
            label4.after(1000, lambda: label4.configure(text=password, text_color="#5bff8f"))
        
        label4.bind("<Button-1>", copy_to_clipboard)

    except ValueError as e:
        print(e)
        label3.pack(pady=20, padx=20)
    
def main():

    root = CTk()
    root.title("Password Gen")
    root.geometry("500x350")
    root.configure(fg_color="#353535")
    root.resizable(width=False, height=False)
    root.minsize(500, 350)
    root.maxsize(500, 350)

    # Frames 
    frame = CTkFrame(root, fg_color="#252525", width=600, height=400)

    frame2 = CTkFrame(root, fg_color="#353535", width=600)
    frame2.pack(pady=10, padx=10, side=TOP)

    # Labels
    label1 = CTkLabel(frame2, text="Enter the length for the password: ", font=("Arial", 20), text_color="white")
    label1.pack(pady=10, padx=10, side=TOP)
    
    label2 = CTkLabel(frame, text="Created by ne0mesys", font=("Arial", 14), text_color="white")
    label2.pack(anchor="nw", pady=5, padx=10)

    label3 = CTkLabel(frame, text="Error: You must write the length in NUMBERS!", text_color="red", font=("Arial", 20))

    label4 = CTkLabel(frame, text_color="#5bff8f", font=("Arial", 18), cursor="hand2") 

    # Entries
    entry1 = CTkEntry(frame2, width=70, corner_radius=5, placeholder_text="Ex: 20", font=("Arial", 18), text_color="#FFFFFF", border_color="white")
    entry1.pack(pady=10, padx=10)

    # Switches .get() --> Gets value of switch to check the option
    switch = CTkSwitch(frame2, width=10, text="Special Characters", progress_color="#00ffe3", button_color="white", hover=False, button_hover_color="#979797", onvalue=1, font=("Arial", 15, "bold"), text_color="white")
    switch.pack(pady=10, padx=10, side=RIGHT)

    # Buttons
    button1 = CTkButton(frame2, width=100, corner_radius=5, fg_color="#00ffe3", hover_color="#d3f3fa", text_color="black", text="Generate", font=("Arial", 15,), command=lambda: generate(entry1, frame, label3, label4, char, char_special, root, switch))
    button1.pack(pady=10, padx=10)

    frame.pack(pady=10, padx=10, side=BOTTOM)
    frame.pack_propagate(False)

    # Chars
    char_special = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "·", "$", "%", "&", "/", "(", ")", "=", "_", "-", ".", ",", ":", ";", "?", "¿", "¡", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    root.mainloop()


if __name__ == '__main__':
    main()
    signal.signal(signal.SIGINT, def_handler)

