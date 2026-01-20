import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import requests
import schedule
import time

# ================= TEXT TO SPEECH =================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ================= SPEECH RECOGNIZER =================
recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

# ================= FEATURES =================
def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_web(query):
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
    else:
        speak("Please tell me what to search.")

def get_weather(city="Hyderabad"):
    api_key = "c36c333fcec8024224329fd55d21239e"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url).json()
        if response.get("main"):
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            speak(f"The temperature in {city} is {temp} degree celsius with {desc}")
        else:
            speak("Unable to get weather report.")
    except:
        speak("Weather service error.")

def set_reminder(task, delay=1):
    def reminder():
        speak(f"Reminder: {task}")
    schedule.every(delay).minutes.do(reminder)

def answer_question(query):
    try:
        info = wikipedia.summary(query, sentences=2)
        speak(info)
    except:
        speak("I couldn't find an answer.")

# ================= RESPONSE LOGIC =================
def respond(command):
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command or "day" in command:
        tell_date()

    elif "search" in command or "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        search_web(query)

    elif "weather" in command or "temperature" in command:
        get_weather()

    elif "remind" in command:
        set_reminder("Do your homework", 1)
        speak("Reminder set for one minute.")

    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "").strip()
        answer_question(query)

    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye. Have a nice day.")
        exit()

    else:
        speak("Sorry, I don't understand that yet.")

# ================= MAIN LOOP =================
if __name__ == "__main__":
    speak("Voice Assistant Activated.")

    while True:
        command = listen()
        if command:
            respond(command)

        schedule.run_pending()
        time.sleep(1)

