import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia


class SmartAssistant:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 165)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greeting(self):
        hour = datetime.datetime.now().hour

        if hour < 12:
            self.speak("Good morning")
        elif hour < 18:
            self.speak("Good afternoon")
        else:
            self.speak("Good evening")

        self.speak(
            "I am Pujii, a smart voice assistant created by Charan Tej. How can I help you?"
        )

    def listen(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="en-IN")
            print("You said:", command)
            return command.lower()
        except:
            self.speak("Sorry, I did not understand that. Please try again.")
            return ""

    def tell_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")

    def tell_date(self):
        today_date = datetime.datetime.now().strftime("%d %B %Y")
        self.speak(f"Today's date is {today_date}")

    def wikipedia_search(self, topic):
        try:
            result = wikipedia.summary(topic, sentences=2)
            self.speak(result)
        except:
            self.speak("Sorry, I could not find information on that topic.")

    def open_youtube(self):
        self.speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    def google_search(self, topic):
        self.speak("Searching on Google")
        webbrowser.open("https://www.google.com/search?q=" + topic)

    def start(self):
        self.greeting()

        while True:
            command = self.listen()

            if command == "":
                continue

            elif "hello" in command:
                self.speak("Hello! Nice to talk to you.")

            elif "who are you" in command:
                self.speak(
                    "I am a smart voice assistant developed by Charan Tej."
                )

            elif "your name" in command:
                self.speak("My name is Pujii.")

            elif "time" in command:
                self.tell_time()

            elif "date" in command:
                self.tell_date()

            elif "wikipedia" in command:
                topic = command.replace("wikipedia", "").strip()
                self.speak("Searching Wikipedia")
                self.wikipedia_search(topic)

            elif "open youtube" in command:
                self.open_youtube()

            elif "search" in command:
                topic = command.replace("search", "").strip()
                self.google_search(topic)

            elif "exit" in command or "stop" in command:
                self.speak("Thank you. Have a great day.")
                break

            else:
                self.speak("This command is not supported yet.")


if __name__ == "__main__":
    assistant = SmartAssistant()
    assistant.start()

