import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Arquivos")
        self.current_dir = os.getcwd()

        self.create_widgets()

    def create_widgets(self):
        self.label_dir = tk.Label(self.root, text="Diretório Atual:")
        self.label_dir.pack()

        self.listbox = tk.Listbox(self.root, width=50, height=20)
        self.listbox.pack()

        self.update_listbox()

        self.button_open = tk.Button(self.root, text="Abrir", command=self.open_file)
        self.button_open.pack()

        self.button_up = tk.Button(self.root, text="Subir", command=self.up_directory)
        self.button_up.pack()

        self.button_exit = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.button_exit.pack()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in os.listdir(self.current_dir):
            self.listbox.insert(tk.END, item)

    def open_file(self):
        selected_item = self.listbox.curselection()
        if selected_item:
            selected_item = selected_item[0]
            filename = self.listbox.get(selected_item)
            file_path = os.path.join(self.current_dir, filename)
            if os.path.isfile(file_path):
                os.startfile(file_path)
            else:
                messagebox.showinfo("Aviso", "Selecione um arquivo válido.")
        else:
            messagebox.showinfo("Aviso", "Selecione um arquivo.")

    def up_directory(self):
        self.current_dir = os.path.abspath(os.path.join(self.current_dir, os.pardir))
        self.update_listbox()
        self.label_dir.config(text="Diretório Atual: " + self.current_dir)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()
