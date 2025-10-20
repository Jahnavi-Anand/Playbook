# 📘 PDF to Audio Converter

Convert any **PDF file into an MP3 audio file** using Python!  
This script extracts text from a PDF using **PyPDF2** and converts it to speech using **pyttsx3**.

---

## 🧰 Requirements

- Python **3.12+**
- The following libraries:
```bash
  pip install PyPDF2 pyttsx3
```

---

## 🚀 How to Use

1. Clone or download this repository.
2. Place your PDF (e.g., `file.pdf`) in the same directory as `index.py`.
3. Update the file path in your script if needed:

   ```python
   output_path = r"<YOUR_FULL_PATH>\audio.mp3"
   ```
4. Open a terminal in the project directory and run:

   ```bash
   python index.py
   ```

The program will:

* Read your PDF file
* Convert its text into spoken words
* Save the output as an MP3 file at the specified path

---

## 📁 Example Project Structure

```
Playbook/
├── file.pdf
├── index.py
├── README.md
└── audio.mp3
```

---

## ⚙️ Notes

* Works best with **text-based PDFs** (not scanned images).
* For scanned PDFs, consider using OCR tools like `pytesseract`.
* You can modify the voice, speed, or output file name in the script using the `pyttsx3` settings.

---

## 🧑‍💻 Author

**Jahnavi Anand**
Built with 💜 in Python.

---

## 🪪 License

This project is licensed under the **MIT License** — free to use and modify.
