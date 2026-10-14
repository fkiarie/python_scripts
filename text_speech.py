from gtts import gTTS

def text_to_speech(text, lang='en', filename='output.mp3'):
    """
    Convert text to speech and save it as an audio file.

    Parameters:
    text (str): The text to convert to speech.
    lang (str): The language for the speech (default is 'en' for English).
    filename (str): The name of the output audio file (default is 'output.mp3').
    """
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Audio saved as {filename}")

text = "Hello, this is a text to speech conversion example."
text_to_speech(text)
