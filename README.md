# PDF to Audio Converter 🎧

A simple Python script that converts any PDF file into speech and saves it as an MP3 audio file.  
It uses **PyPDF2** to extract text from PDFs and **pyttsx3** for text-to-speech conversion.

---

## 📦 Installation

Make sure you have **Python 3.12+** installed.  
Then install the required libraries:

```bash
pip install PyPDF2 pyttsx3
```
🚀 Usage
Place your PDF file (e.g., file.pdf) in the same directory as index.py.

Open a terminal in that folder.

Run the script:

bash
Copy code
python index.py
The program will:

Read all pages of your file.pdf

Convert the text to speech

Save the audio as audio.mp3 in the same folder

🧩 File Structure
css
Copy code
Playbook/
├── file.pdf
├── index.py
├── audio.mp3
└── README.md
⚙️ Notes
Ensure your PDF contains selectable text (not scanned images).

For scanned PDFs, you’ll need OCR tools like pytesseract.

You can change the output file path inside the script if needed.

Author: Jahnavi
License: MIT
