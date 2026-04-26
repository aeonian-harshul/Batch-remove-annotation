# PDF Batch Annotation Remover

A simple, beginner-friendly Python script that removes annotations (like highlights, comments, and drawings) from a whole folder of PDF files at once, while **keeping all internal document hyperlinks completely intact**. 

This is perfect for cleaning up heavily marked-up documents without breaking their navigation.

## ✨ Features
* **Batch Processing:** Point it at a folder, and it processes every PDF inside automatically.
* **Smart Cleaning:** Deletes standard annotations but preserves `/Link` subtypes so your clickable table of contents and cross-references still work.
* **Non-Destructive:** Your original files are never touched. The script creates brand new copies with a `cleaned_` prefix.
* **Beginner Friendly:** No command-line arguments needed. Just run the script and drag-and-drop your folder into the window!

## 🛠️ Prerequisites
To use this script, you will need to have **Python** installed on your computer.
* Download Python here: [python.org/downloads](https://www.python.org/downloads/)
* *Note for Windows Users: When installing, make sure to check the box that says **"Add Python to PATH"** at the bottom of the installer window.*

## 🚀 Installation

1. **Download the script:** Download the `cleaner.py` file to your computer (e.g., to your Desktop).
2. **Install the required library:** This script relies on the `pdfrw` library to read and write PDFs. Open your terminal (Mac) or Command Prompt (Windows) and run the following command:
   ```text
   pip install pdfrw

## 📖 How to Use

1. Double-click the `cleaner.py` file to run it.
2. A terminal window will open asking for your folder path.
3. Simply **drag and drop** the folder containing your PDFs directly into the window and press **Enter**.
4. The script will scan the folder and generate clean copies of your PDFs inside that exact same folder. 

## ⚠️ Notes
* **Always make a backup:** You can try it with 1 PDF file first or keep a backup folder just in case the script breaks the PDFs.
* Files that already start with `cleaned_` will be skipped to prevent infinite loops.
* If a PDF is password-protected or heavily encrypted, the script may skip it and print an error message to let you know.

## 🙏 Acknowledgements

This script was adapted from a command-line utility to be more accessible for non-programmers via a simple drag-and-drop interface. Built using the `pdfrw` library. Gemini was used in the process to write the python code,
