
# 🔐 Mini Ransomware Simulator (Educational Project)

This is a **simple ransomware simulation** project written in Python to demonstrate how file encryption and decryption works using symmetric key cryptography. The purpose of this project is strictly **educational** — to help students and ethical hackers understand the behavior of ransomware in a safe environment.

---

## ⚠️ Disclaimer

> This code is intended for **educational purposes only**.  
> **Do NOT** use it on any computer or system that you do not own or have explicit permission to test.  
> Unauthorized use of this code may be illegal and unethical.

---

## 📁 Project Structure

```
.
├── ransom.py       # Encrypts all files in the current directory
├── decrypt.py      # Decrypts encrypted files using a key and passphrase
├── thekey.key      # Stores the generated encryption key
```

---

## 🛠 Features

- 🔍 Scans the current directory and selects files for encryption
- 🔐 Encrypts files using the `cryptography` module (Fernet symmetric encryption)
- 🔑 Generates and stores an encryption key in `thekey.key`
- 🧾 Displays a simulated ransom note after encryption
- 🔓 Decrypts files using the same key with a passphrase check

---

## 🧪 How to Use

> Only test this in a safe, controlled environment like a virtual machine or isolated folder.

### 1. Install Required Dependency

Make sure Python 3 is installed, then install the `cryptography` module:

```bash
pip install cryptography
```

### 2. Add Test Files

Place a few sample files (e.g., `.txt`, `.md`, etc.) in the same directory as the scripts to test encryption and decryption.

### 3. Run the Ransomware Simulation

```bash
python3 ransom.py
```

- This will encrypt all files in the folder except `ransom.py`, `decrypt.py`, and `thekey.key`.
- You will see a ransom-style message printed in the terminal.

### 4. Decrypt Files

```bash
python3 decrypt.py
```

- You'll be asked to enter a secret phrase.  
- Enter: `coffee`  
- If correct, files will be decrypted. If not, you'll receive a simulated ransom denial.

---

## 🔒 Encryption/Decryption Details

- **Encryption** is done using the `Fernet` algorithm from the `cryptography` library.
- A new encryption key is generated each time `ransom.py` is executed.
- The key is stored in a file called `thekey.key`.
- Decryption is only possible if:
  - The correct key is available in `thekey.key`
  - The correct passphrase (`coffee`) is provided by the user

---

## 💡 Purpose

This mini project is ideal for:

- Learning how ransomware encrypts files
- Understanding basic cryptographic operations in Python
- Practicing ethical hacking in CTF or cyber labs
- Raising awareness about ransomware attacks

---

## 📜 License

MIT License — free to use for **educational and ethical hacking purposes**.

---

## 👨‍💻 Author

Developed by Umair Saeed  
Inspired by cybersecurity research and malware analysis for ethical hackers.

---

## 🧠 Reminder

Always use cybersecurity tools responsibly. The best hackers are the ones who protect systems, not break them.