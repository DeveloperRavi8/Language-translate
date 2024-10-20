# Import necessary modules
import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Initialize the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("800x400")
root.config(bg="lightblue")  # Set the background color

# Create a Translator instance
translator = Translator()

# Title label
title_label = tk.Label(root, text="LANGUAGE TRANSLATOR", bg="lightblue",
                       font=("Helvetica", 18, "bold"))
title_label.place(x=300, y=20)

# 'Enter Text' label
input_label = tk.Label(root, text="Enter Text", bg="lightblue",
                       font=("Helvetica", 14))
input_label.place(x=10, y=80)

# Text area for entering input text
input_text = tk.Text(root, font=("Helvetica", 12), height=5, width=30, wrap=tk.WORD, bd=0, padx=10, pady=10)
input_text.place(x=10, y=120)

# 'Select Input Language' label
input_lang_label = tk.Label(root, text="Input Language", bg="lightblue",
                            font=("Helvetica", 12))
input_lang_label.place(x=70, y=290)

# Combobox for input languages
input_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Helvetica", 12))
input_lang_combo.place(x=150, y=290)
input_lang_combo.set("english")  # Default value

# 'Select Output Language' label
output_lang_label = tk.Label(root, text="Output Language", bg="lightblue",
                             font=("Helvetica", 12))
output_lang_label.place(x=400, y=290)

# Combobox for output languages
output_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Helvetica", 12))
output_lang_combo.place(x=500, y=290)
output_lang_combo.set("hindi")  # Default value

# Function to perform translation
def translate_text():
    input_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(input_lang_combo.get())]
    output_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(output_lang_combo.get())]
    translated = translator.translate(input_text.get("1.0", tk.END), src=input_lang, dest=output_lang)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated.text)

translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Helvetica", 12), bg="lightgreen")
translate_button.place(x=350, y=350)

output_text = tk.Text(root, font=("Helvetica", 12), height=5, width=30, wrap=tk.WORD, bd=0, padx=10, pady=10)
output_text.place(x=400, y=120)

# Run the application
root.mainloop()
