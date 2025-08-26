from gtts import gTTS
import PyPDF2

# Open PDF
pdf_file = open("Custos-tasks.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract all text
text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

# Convert to speech
tts = gTTS(text=text, lang="en")
tts.save("audiobook.mp3")

print("✅ Voice-over saved as audiobook.mp3")
