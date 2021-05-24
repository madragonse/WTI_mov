from gtts import gTTS



def generate_mp3(text:str, launguage="pl"):
    tts = gTTS(text, lang=launguage)
    tts.save('static/hello.mp3')