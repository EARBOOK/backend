from gtts import gTTS 
import os
import speech_recognition as sr 

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice =listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        if 'play Adventures of Huckleberry Finn' in command:
            f=open('book11.txt', 'r')
            data =f.read()
            
            myText =data

            language ='en'

            output =gTTS(text=myText, lang =language, slow=False)

            output.save("out.mp3")
            os.system("start out.mp3")
        elif 'play book 2' in command:
            f=open('book2.txt', 'r')
            data1 =f.read()
            
            myText1 =data1

            language ='en'

            output1 =gTTS(text=myText1, lang =language, slow=False)

            output1.save("out1.mp3")
            os.system("start out1.mp3")
        elif 'play book 3' in command:
            f=open('book13.txt', 'r')
            data =f.read()
            
            myText =data

            language ='en'

            output =gTTS(text=myText, lang =language, slow=False)

            output.save("out2.mp3")
            os.system("start out2.mp3")




except:
    pass