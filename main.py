import spacy
import json
import re
import tkinter as tk
from tkinter import messagebox

nlp = spacy.load("en_core_web_sm")

with open("data/word_mapping.json", "r") as file:
    translation_dict = json.load(file)

def translation(text):
    doc = nlp(text)

    transformed_tokens = []

    for token in doc:
        # Check if token is in the dictionary and replace it
        if token.text.lower() in translation_dict:
            transformed_token = translation_dict[token.text.lower()]
        else:
            transformed_token = token.text

        # Append the token
        transformed_tokens.append(transformed_token)

    # Join the tokens
    transformed_text = ' '.join(transformed_tokens)

    # Remove unnecessary extra spaces around punctuation
    transformed_text = re.sub(r'\s([,!.?;])', r'\1', transformed_text)
    transformed_text = re.sub(r'\s+-\s+', '-', transformed_text)  
    transformed_text = re.sub(r"'\s", "'", transformed_text)

    # Capitalize the first letter of sentences
    transformed_text = re.sub(r'([.!?])\s*(\w)', lambda m: m.group(1) + ' ' + m.group(2).upper(), transformed_text)

    # Capitalize starting letter of overall text
    transformed_text = transformed_text[0].upper() + transformed_text[1:]

    return transformed_text.strip()

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