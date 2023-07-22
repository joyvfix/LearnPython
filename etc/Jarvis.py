import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the speech recognition service.")
        return ""

# Main function to run the AI assistant


def run_ai_assistant():
    while True:
        query = listen()

        if query:
            if "hello" in query:
                speak("Hello! How can I assist you?")
            elif "what is your name" in query:
                speak("My name is AI Assistant.")
            elif "how are you" in query:
                speak("I'm fine, thank you!")
            elif "quit" in query or "exit" in query:
                speak("Goodbye!")
                exit()
            else:
                speak("I'm sorry, I can't help with that.")


if __name__ == "__main__":
    run_ai_assistant()
