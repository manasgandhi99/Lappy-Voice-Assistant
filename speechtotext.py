import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognized_text = r.recognize_google(text)
        print(recognized_text)
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError as e:
        print(e)

        