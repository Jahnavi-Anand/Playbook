import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfReader(open('file.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()

output_path = r"C:\sonar-scanner-5.0.1.3006-windows\bin\Playbook\audio.mp3"
speaker.save_to_file(text, output_path)
speaker.runAndWait()