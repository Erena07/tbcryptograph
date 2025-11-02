import tkinter as tk
from gost import gost_encrypt, gost_decrypt
from utils import pad_key

def run_gui():
    root = tk.Tk()
    root.title("GOST 28147-89 Encryption Tool")
    root.geometry("400x350")
    root.configure(bg="#202020")

    tk.Label(root, text="Plaintext:", bg="#202020", fg="white").pack()
    entry_plain = tk.Text(root, height=5, width=45)
    entry_plain.pack()

    tk.Label(root, text="Key:", bg="#202020", fg="white").pack()
    entry_key = tk.Entry(root, width=40, show="*")
    entry_key.pack()

    result_box = tk.Text(root, height=5, width=45, state='disabled')
    result_box.pack(pady=10)

    def encrypt_action():
        text = entry_plain.get("1.0", tk.END).strip().encode()
        key = pad_key(entry_key.get())
        cipher = gost_encrypt(text, key)
        result_box.config(state='normal')
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, cipher.hex())
        result_box.config(state='disabled')

    def decrypt_action():
        text = bytes.fromhex(entry_plain.get("1.0", tk.END).strip())
        key = pad_key(entry_key.get())
        plain = gost_decrypt(text, key).decode(errors='ignore')
        result_box.config(state='normal')
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, plain)
        result_box.config(state='disabled')

    tk.Button(root, text="Encrypt", command=encrypt_action, width=15).pack(side="left", padx=20, pady=10)
    tk.Button(root, text="Decrypt", command=decrypt_action, width=15).pack(side="right", padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
