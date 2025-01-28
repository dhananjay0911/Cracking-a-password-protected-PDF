import tkinter as tk
from tkinter import filedialog, messagebox
import itertools
import threading
import PyPDF2

# Global variable for the selected PDF path
pdf_path = None

# Function to attempt to unlock the encrypted PDF
def unlock_pdf(key):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            if reader.is_encrypted:
                try:
                    reader.decrypt(key)
                    reader.pages[0]  # Try to read the first page
                    return True  # Successful decryption
                except:
                    return False  # Decryption failed
            else:
                messagebox.showinfo("Info", "This PDF is not password protected.")
                return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

# Numeric brute-force attack for 6-digit passwords
def brute_force_attack():
    characters = "0123456789"  # Only numeric characters
    for key_tuple in itertools.product(characters, repeat=6):
        key = ''.join(key_tuple)
        if unlock_pdf(key):
            cracked_password.set(key)  # Set the cracked password in the entry
            messagebox.showinfo("Success", f"Password found: {key}")
            return

    messagebox.showinfo("Result", "Brute-force attack completed, password not found.")

# Function to start the brute-force attack
def start_attack():
    threading.Thread(target=brute_force_attack).start()

# Function to select the PDF file
def select_pdf():
    global pdf_path
    pdf_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        selected_file_label.config(text=f"Selected File: {pdf_path.split('/')[-1]}")
    else:
        selected_file_label.config(text="No file selected")

# Setup the GUI window
root = tk.Tk()
root.title("Numeric PDF Password Cracker")

# Button to select the PDF file
select_pdf_button = tk.Button(root, text="Select PDF", command=select_pdf)
select_pdf_button.pack(pady=10)

# Label to show selected file
selected_file_label = tk.Label(root, text="No file selected")
selected_file_label.pack(pady=5)

# Label for showing the cracked password
cracked_password_label = tk.Label(root, text="Cracked Password:")
cracked_password_label.pack(pady=5)
cracked_password = tk.StringVar()
cracked_password_entry = tk.Entry(root, textvariable=cracked_password, width=40, state='readonly')
cracked_password_entry.pack(pady=5)

# Button to start the attack
attack_button = tk.Button(root, text="Start Attack", command=start_attack)
attack_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
