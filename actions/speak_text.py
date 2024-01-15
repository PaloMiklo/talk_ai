def speak_text(text: str, engine: str) -> None:
    engine.say(text)
    engine.runAndWait()