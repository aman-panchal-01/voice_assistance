import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "None"
def handle_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "search" in command:
        speak("What should I search for?")
        search_query = listen()
        if search_query != "None":
            speak(f"Searching for {search_query} on Google.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I am not sure how to help with that.")
if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        user_command = listen()
        if user_command != "None":
            handle_command(user_command)
