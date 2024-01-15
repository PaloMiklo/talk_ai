import speech_recognition as sr

def recognize_speech(recognizer: any, microphone: any) -> any:
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "I didn't catch that. Please speak again."
    except sr.RequestError:
        return "There was an error with the speech recognition service."