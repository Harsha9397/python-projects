from gtts import gTTS
file = open("demo.txt","r",encoding="utf-8").read()
language = "en"
speech = gTTS(text=str(file),lang=language,slow=False)
speech.save("audio.mp3")