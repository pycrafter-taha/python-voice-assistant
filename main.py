import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def pcommand(c):
    if(c.lower() == 'open google'):
        webbrowser.open('https://google.com')
    elif(c.lower() == 'open stackoverflow'):
        webbrowser.open('https://stackoverflow.com/questions')
    elif(c.lower() == 'open amazon'):
        webbrowser.open('https://amazon.in')

if __name__ == '__main__':
    speak('Initializing Nova....')

while True:
    r = sr.Recognizer()



    print('Recognizing...')

    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)
        word = r.recognize_google(audio)
        if(word.lower() == 'nova'):
            speak('At your Service SIR!!')

            with sr.Microphone() as source: 
                print('Nova Active...')
                audio = r.listen(source)
                command = r.recognize_google(audio)
                pcommand(command)

    except Exception as e:
        print('error; {0}'.format(e))

