import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import time
import schedule

# ================== SETUP ==================
# Text-to-Speech engine
speech = pyttsx3.init()
speech.setProperty("rate", 170) 
engine.setProperty("volume", 1.0) 
# Your API Keys (Replace with real ones)
WEATHER_API_KEY = "84aa021ba37c4900b3f143632252509"
NEWS_API_KEY = "04ecadc15ddb4b909f0b2a3e93e966fc"

# ================== FUNCTIONS ==================
def speak(text):
    """Convert text to speech"""
    print("Assistant:", text)
    speech.say(text)
    speech.runAndWait()

def listen():
    """Listen to voice input and return as text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=5)

    try:
        query = r.recognize_google(audio)
        print("You:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Network error. Check your internet.")
        return ""

def get_weather(city="Hyderabad"):
    """Fetch weather using OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return "I couldn't fetch the weather right now."
    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    return f"The weather in {city} is {desc} with {temp}°C."

def get_news():
    """Fetch top 3 news headlines"""
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    if res.get("status") != "ok":
        return "I couldn't fetch the news right now."
    articles = res["articles"][:3]
    headlines = [a["title"] for a in articles]
    return "Here are the top news: " + "; ".join(headlines)

def set_reminder(text, seconds=10):
    """Set a simple reminder"""
    def remind():
        speak(f"Reminder: {text}")
    schedule.every(seconds).seconds.do(remind)
    speak(f"Reminder set for {seconds} seconds from now.")

def open_website(site):
    """Open a website"""
    speak(f"Opening {site}")
    webbrowser.open(f"https://{site}.com")

# ================== MAIN LOOP ==================
def main():
    speak("Hello! I am your assistant. How can I help you?")
    while True:
        query = listen()
        if not query:
            continue

        # Exit
        if "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye!")
            break

        # Weather
        elif "weather" in query:
            city = "Hyderabad"
            if "in" in query:
                city = query.split("in")[-1].strip()
            speak(get_weather(city))

        # News
        elif "news" in query:
            speak(get_news())

        # Reminder
        elif "remind" in query:
            set_reminder("Drink water!", 10)  # fixed for demo

        # Open website
        elif "open" in query:
            site = query.replace("open", "").strip()
            open_website(site)

        # Time
        elif "time" in query:
            now = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"The time is {now}")

        else:
            speak("I can check weather, read news, set reminders, or open websites.")

        # Run scheduled reminders
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
