# Cracking-a-password-protected-PDF
A Python project designed to crack password-protected PDF files using brute force or dictionary attacks. It utilizes libraries like PyPDF2 or pikepdf to test multiple password combinations and unlock secured PDF files.


**Overview
This project is a simple Numeric PDF Password Cracker built using Python and Tkinter. It performs a brute-force attack to unlock password-protected PDF files with 6-digit numeric passwords. The tool iterates through all possible 6-digit numeric combinations to decrypt the PDF.**

**Features**
Select and load a PDF file using a graphical user interface (GUI).
Brute-force attack for 6-digit numeric passwords (e.g., 000000 to 999999).
Displays the cracked password if found.
User-friendly interface with progress updates and notifications.
Uses multithreading to ensure the application remains responsive during the attack.

**Requirements**
Python 3.x
**Libraries:**
tkinter (built-in with Python)
itertools (built-in with Python)
threading (built-in with Python)
PyPDF2

**Install the required library using the following command:**
pip install PyPDF2

**How to Use**
Clone or download the repository.

**Install the required Python libraries.**

**Run the script using the following command:**
python pdf_password_cracker.py
Use the "Select PDF" button to choose a password-protected PDF file.

Click "Start Attack" to begin the brute-force attack for 6-digit numeric passwords.

If the password is successfully found, it will be displayed in the "Cracked Password" field.

If the password is not found or the PDF is not encrypted, a message will notify the user.

**Code Details
GUI Design:**
Built using Tkinter, the interface includes buttons, labels, and entry fields for interacting with the application.
**PDF Decryption:**
The decryption process uses the PyPDF2 library to attempt unlocking the PDF with every 6-digit numeric combination.
**Brute-force Logic:**
The itertools.product function generates all possible 6-digit numeric combinations.
Each combination is tested against the encrypted PDF until the correct password is found or all combinations are exhausted.
Multithreading:

The attack process runs in a separate thread using the threading module to prevent the GUI from freezing during long operations.

**Sample Output**
If the password is found:
Success: Password found: 123456
If the PDF is not encrypted:
Info: This PDF is not password protected.
If the password is not found after all combinations:
Result: Brute-force attack completed, password not found.

**Disclaimer**
This tool is intended for educational purposes only. Please use it responsibly and only on PDF files that you own or have explicit permission to test. Unauthorized use on other files may violate ethical and legal boundaries.

**Future Enhancements**
Add support for alphanumeric passwords.
Display progress and estimated time remaining for the brute-force attack.
Include a feature to allow custom wordlists for dictionary-based attacks.
Contributors
If you have suggestions or improvements, feel free to submit a pull request or open an issue!
