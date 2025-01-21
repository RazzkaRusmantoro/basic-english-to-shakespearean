import tkinter as tk
from tkinter import messagebox
from translation_logic import translation

def on_enter(event, user_input_entry, root):
    user_input = user_input_entry.get("1.0", "end-1c")
    if user_input:
        shakespearean_text = translation(user_input)
        messagebox.showinfo("Shakespearean Translation", shakespearean_text)
    root.quit()

def main():
    root = tk.Tk()
    root.geometry("600x200")

    label = tk.Label(root, text="Enter text in English:")
    label.pack(pady=10)

    user_input_text = tk.Text(root, width=60, height=8)
    user_input_text.pack(pady=0)
    
    user_input_text.bind('<Return>', lambda event: on_enter(event, user_input_text, root))

    root.mainloop()

if __name__ == "__main__":
    main()
