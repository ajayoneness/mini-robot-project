import speech_recognition as sr
import wikipedia
from gtts import gTTS
from playsound import playsound

#recording part
for i in range(1,10):
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("clearing backgroung noise.....")
        rec.adjust_for_ambient_noise(source, duration=1)
        print("weating for your message : ")
        recaudio = rec.listen(source)
        print("recording done... !")
    try:
        # recording to text converting part
        print("printing the message ....")
        text = rec.recognize_google(recaudio, language='hindi-IN')
        print(f"your messange is : {format(text)}")

        # listining part
        topic = (f"searching for ---> {format(text)}")
        summ = wikipedia.summary(topic)
        print(summ)
        tts = gTTS(summ)
        tts.save(f"wiki{format(text)}.mp3")

        # reading audio file
        print("reading.....")
        playsound(f"wiki{format(text)}.mp3")

    except:
        print("keyword is not found !!")

