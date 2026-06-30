
#! Jarvis - Python AI Assistant

import os
from dotenv import load_dotenv

load_dotenv()

import pyttsx3
import threading
import datetime
import webbrowser
import os
import smtplib
import requests
import schedule
import time
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ──────────────────────────────────────────────
#  CONFIG  — fill these in
# ──────────────────────────────────────────────
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY  = os.getenv("WEATHER_API_KEY")
EMAIL_ADDRESS    = os.getenv("GMAIL_ADDRESS")
EMAIL_PASSWORD   = os.getenv("GMAIL_APP_PASSWORD")       # Gmail app password, not your real password

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


# ──────────────────────────────────────────────
#  SPEAK
# ──────────────────────────────────────────────
def speak(text):
    print("Jarvis:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine


# ──────────────────────────────────────────────
#  WEATHER
# ──────────────────────────────────────────────
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()
        if data["cod"] != 200:
            speak("I couldn't find that city.")
            return
        temp        = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The weather in {city} is {description} with a temperature of {temp} degrees Celsius.")
    except:
        speak("Sorry, I couldn't fetch the weather right now.")


# ──────────────────────────────────────────────
#  WEB SEARCH
# ──────────────────────────────────────────────
def search_web(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")


# ──────────────────────────────────────────────
#  OPEN APPS / WEBSITES
# ──────────────────────────────────────────────
APPS = {
    "notepad"  : "notepad.exe",
    "calculator": "calc.exe",
    "paint"    : "mspaint.exe",
    "vs code"  : "code",
    "chrome"   : "chrome",
}

SITES = {
    "youtube"  : "https://youtube.com",
    "github"   : "https://github.com",
    "google"   : "https://google.com",
    "whatsapp" : "https://web.whatsapp.com",
}

def open_app_or_site(user_input):
    for site, url in SITES.items():
        if site in user_input:
            webbrowser.open(url)
            speak(f"Opening {site}")
            return
    for app, cmd in APPS.items():
        if app in user_input:
            os.system(f"start {cmd}")
            speak(f"Opening {app}")
            return
    speak("Sorry, I don't know how to open that.")


# ──────────────────────────────────────────────
#  JOKES
# ──────────────────────────────────────────────
def tell_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        joke = f"{response['setup']} ... {response['punchline']}"
        speak(joke)
    except:
        speak("Why do programmers prefer dark mode? Because light attracts bugs!")


# ──────────────────────────────────────────────
#  REMINDERS
# ──────────────────────────────────────────────
def set_reminder(user_input):
    try:
        # expects: "remind me in X minutes to <task>"
        parts   = user_input.split("in")[1].split("minutes to")
        minutes = int(parts[0].strip())
        task    = parts[1].strip()

        def reminder_job():
            speak(f"Reminder! {task}")

        schedule.every(minutes).minutes.do(reminder_job).tag("one-time")
        speak(f"Got it! I'll remind you to {task} in {minutes} minutes.")

        # run scheduler in background
        def run_scheduler():
            while True:
                schedule.run_pending()
                # cancel after first run (one-time reminder)
                for job in schedule.get_jobs("one-time"):
                    if job.last_run is not None:
                        schedule.cancel_job(job)
                time.sleep(1)

        t = threading.Thread(target=run_scheduler, daemon=True)
        t.start()
    except:
        speak("Please say something like: remind me in 5 minutes to drink water")


# ──────────────────────────────────────────────
#  SEND EMAIL
# ──────────────────────────────────────────────
def send_email():
    try:
        speak("Who should I send the email to? Please type the address.")
        to_addr = input("To: ").strip()

        speak("What is the subject?")
        subject = input("Subject: ").strip()

        speak("What should the email say?")
        body = input("Body: ").strip()

        msg = MIMEMultipart()
        msg["From"]    = EMAIL_ADDRESS
        msg["To"]      = to_addr
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_addr, msg.as_string())

        speak("Email sent successfully!")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")
        print("Error:", e)


# ──────────────────────────────────────────────
#  AI RESPONSE (GEMINI)
# ──────────────────────────────────────────────
def ask_gemini(query):
    try:
        speak("Let me think...")
        response = model.generate_content(query)
        answer   = response.text.strip()
        # trim long responses for speech
        if len(answer) > 300:
            spoken = answer[:300] + "... I've printed the full answer above."
        else:
            spoken = answer
        print("\n--- Gemini ---\n", answer, "\n--------------\n")
        speak(spoken)
    except Exception as e:
        speak("Sorry, I couldn't get a response from Gemini.")
        print("Error:", e)


# ──────────────────────────────────────────────
#  MAIN LOOP
# ──────────────────────────────────────────────
speak("Hello! I am Jarvis, your AI assistant. How can I help you?")

while True:
    user_input = input("👤 You: ").lower().strip()

    if not user_input:
        continue

    elif user_input == "exit":
        speak("Goodbye! Have a great day.")
        break

    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! How may I assist you today?")

    elif "how are you" in user_input:
        speak("I am just a bot, but I'm running perfectly!")

    elif "your name" in user_input or "who are you" in user_input:
        speak("I am Jarvis, your personal AI assistant.")

    elif "time" in user_input:
        t = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {t}")

    elif "date" in user_input:
        d = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {d}")

    elif "weather" in user_input:
        speak("Which city?")
        city = input("City: ").strip()
        get_weather(city)

    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        if not query:
            speak("What should I search for?")
            query = input("Search: ").strip()
        search_web(query)

    elif "open" in user_input:
        open_app_or_site(user_input)

    elif "joke" in user_input:
        tell_joke()

    elif "remind" in user_input:
        set_reminder(user_input)

    elif "email" in user_input:
        send_email()

    elif "calculate" in user_input:
        try:
            result = eval(user_input.replace("calculate", "").strip())
            speak(f"The result is {result}")
        except:
            speak("Sorry, I couldn't calculate that.")

    else:
        # fallback to Gemini for anything else
        ask_gemini(user_input)