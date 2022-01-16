from gtts import gTTS
import os
myText = "I am converting text to speech with python"
language = 'en' #language of text 




output =gTTS(text = myText, lang = language, slow= False)

output.save("output.mp3")

os.system("output.mp3")

