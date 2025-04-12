from PyPDF2 import PdfReader
import pyttsx3
reader = PdfReader("datatypesdif.pdf")
number_of_pages = len(reader.pages)
speaker=pyttsx3.init()
page = reader.pages[0]
text = page.extract_text()
speaker.say(text)
speaker.runAndWait()