
import speech_recognition as sr
import pyttsx3
from actions.recognize_speech import recognize_speech
from actions.speak_text import speak_text
from actions.send_message import send_message
from model.mistral import exit

def main() -> None:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()

    while True:
        speech_text = recognize_speech(recognizer, microphone)
        print("You said:", speech_text)
        if speech_text.lower() == exit:
            break

        model_response = send_message(speech_text)
        print("Model:", model_response)
        speak_text(model_response, engine)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated")
