import tkinter as tk
import encryptor

class Application(tk.Frame):
    def __init__(self, master=None):

        super().__init__(master)
        self.master = master

        self.grid()
        self.create_widgets()

    def encrypt(self, plaintext):
        encrypted = encryptor.encrypt_whole(self.public_txt.get(), plaintext.strip())
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, encrypted)
        self.output_text.config(state=tk.DISABLED)

    def decrypt(self, plaintext):
        decrypted = encryptor.decrypt_whole(keydict["private"], plaintext.strip())
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, decrypted)
        self.output_text.config(state=tk.DISABLED)

    def copy_to_clipboard(self, text):
        root.clipboard_clear()
        root.clipboard_append(text)

    def insert_to_input(self, text):
        self.input_text.delete('1.0', tk.END)
        self.input_text.insert(tk.END, text)

    def define_pubkey(self):
        text = root.clipboard_get()
        self.public_txt.set(text)

    def create_widgets(self):
        public_txt_self_label_var = tk.StringVar()
        public_txt_self_label_var.set("Your Address")
        self.public_txt_self_label = tk.Label(self, textvariable=public_txt_self_label_var)
        self.public_txt_self_label.grid(row=0, column=0, sticky='w', pady=5, padx=5)

        self.public_txt_self = tk.StringVar()
        self.public_txt_self.set(keydict["public"])

        public_txt_label_var = tk.StringVar()
        public_txt_label_var.set("Recipient")
        self.public_txt_label = tk.Label(self, textvariable=public_txt_label_var)
        self.public_txt_label.grid(row=1, column=0, sticky='w', pady=5, padx=5)

        self.public_txt = tk.StringVar()
        self.public_txt.set(keydict["public"])

        self.public_entry_self = tk.Entry(self, textvariable=self.public_txt_self, width=130)
        self.public_entry_self.grid(row=0, column=1, sticky='w', pady=5, padx=5)
        self.public_entry_self.config(state=tk.DISABLED)

        self.public_entry = tk.Entry(self, textvariable=self.public_txt, width=130)
        self.public_entry.grid(row=1, column=1, sticky='w', pady=5, padx=5)

        input_text_label_var = tk.StringVar()
        input_text_label_var.set("Input")
        self.input_text_label = tk.Label(self, textvariable=input_text_label_var)
        self.input_text_label.grid(row=2, column=0, sticky='w', pady=5, padx=5)

        self.input_text = tk.Text(self, width=90, height=10)
        self.input_text.grid(row=2, column=1, sticky='EW', pady=5, padx=5)

        output_text_label_var = tk.StringVar()
        output_text_label_var.set("Output")
        self.output_text_label = tk.Label(self, textvariable=output_text_label_var)
        self.output_text_label.grid(row=3, column=0, sticky='w', pady=5, padx=5)

        self.output_text = tk.Text(self, width=90, height=10)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.grid(row=3, column=1, sticky='EW', pady=5, padx=5)

        self.encrypt_button = tk.Button(self, text="Ecrypt", fg="red", command=lambda: self.encrypt(self.input_text.get("1.0", tk.END)))
        self.encrypt_button.grid(row=4, column=1, sticky='EW', padx=5)

        self.decrypt_button = tk.Button(self, text="Decrypt", fg="red", command=lambda: self.decrypt(self.input_text.get("1.0", tk.END)))
        self.decrypt_button.grid(row=5, column=1, sticky='EW', padx=5)

        self.copy_pubkey = tk.Button(self, text="Copy", command=lambda: self.copy_to_clipboard(keydict["public"]))
        self.copy_pubkey.grid(row=0, column=2, sticky='EW', padx=5)

        self.insert_pubkey = tk.Button(self, text="Paste", command=lambda: self.define_pubkey())
        self.insert_pubkey.grid(row=1, column=2, sticky='EW', padx=5)

        self.quit = tk.Button(self, text="Quit", command=lambda: self.master.destroy())
        self.quit.grid(row=8, column=1, sticky='WE', padx=5, pady=(0, 5))

        self.paste_input = tk.Button(self, text="Paste", command=lambda: self.insert_to_input(root.clipboard_get()))
        self.paste_input.grid(row=2, column=2, sticky='EW', padx=5)

        self.copy_output = tk.Button(self, text="Copy", command=lambda: self.copy_to_clipboard(self.output_text.get("1.0", tk.END)))
        self.copy_output.grid(row=3, column=2, sticky='EW', padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("ezcoder")

    if not encryptor.keyfile_found():
        keydict = encryptor.generate()
        encryptor.save(keydict)
    else:
        keydict = encryptor.load()

    app = Application(master=root)
    app.mainloop()