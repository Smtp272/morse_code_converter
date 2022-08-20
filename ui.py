import json
import tkinter
from tkinter import Label, Button, END, Text
import customtkinter
from customtkinter import CTkButton

###CONSTS
headings = ("Montserrat", 15)
textbox_h = 15
textbox_w = 40
bg_color = 'lightgrey'
translate_btn = ("Helvetica", 10, "bold")


class MorseCodeConverter:
    def __init__(self):
        super().__init__()

        ###ROOT
        self.root = customtkinter.CTk()
        self.root.title("Morse code")
        self.root.geometry("900x550")
        self.root.eval('tk::PlaceWindow . center')
        self.root.config(pady=20, padx=20, bg=bg_color)

        ####HEADINGS
        self.original_text = Label(self.root, text="Text", font=headings, bg=bg_color)
        self.original_text.grid(column=0, row=1, sticky="w")
        self.translated_text = Label(self.root, text="Morsecode", font=headings, bg=bg_color)
        self.translated_text.grid(column=2, row=1, sticky="w")

        ####TEXTBOXES
        self.original_textbox = Text(self.root, height=textbox_h, width=textbox_w, font=("Montserrat", 10))
        self.original_textbox.grid(column=0, row=2)

        self.translated_textbox = Text(self.root, height=textbox_h, width=textbox_w, font=("Montserrat", 10, "bold"))
        self.translated_textbox.grid(column=2, row=2)

        ###BUTTONS
        self.translate_button = CTkButton(self.root, text="Translate !", text_font=translate_btn,
                                          command=self._translate_text)
        self.translate_button.grid(column=1, row=2, padx=20)

        self.clear_button = CTkButton(self.root, text="Clear", command=self._clear_textboxes)
        self.clear_button.grid(row=3, column=1, ipadx=5)

        ##RULES
        self.rules_label = Label(self.root,
                                 text="# - Untranslatable character\n/ - Word separator\nSpace - Letter separator",
                                 bg=bg_color, fg="red")
        self.rules_label.grid(row=4, column=1)

        ###MAINLOOP
        self.root.mainloop()

    def _translate_text(self):
        self.translated_textbox.delete(1.0, END)
        words_to_translate = self.original_textbox.get('1.0', 'end')[:-1]
        words_to_translate = words_to_translate.lower()
        with open("code.json", "rb") as file:
            data = json.load(file)['text']
            arr = [MorseCodeConverter.exception_manager(data, i) for i in words_to_translate]
        self.translated_textbox.insert(1.0, " ".join(arr))

    @staticmethod
    def exception_manager(data, a):
        try:
            return data[a]
        except KeyError:
            return "#"

    def _clear_textboxes(self):
        self.translated_textbox.delete(1.0, END)
        self.original_textbox.delete(1.0, END)


if __name__ == "__main__":
    t = MorseCodeConverter()
