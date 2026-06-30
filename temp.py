import pyttsx3
from datetime import datetime

def speak(text):
    print("AI Bot:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine          # <-- fully destroy the object before next call


print("Jarvis: Hello! I am a python AI assistant bot... Type 'exit' to end\n")

while True:
    user_input = input("👤You: ").lower()

    if user_input == "exit":
        speak("Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! I am Jarvis, how may I assist you today?")
    elif "how are you" in user_input:
        speak("I am just a bot, I don't feel emotions.")
    elif "name" in user_input:
        speak("My name is Jarvis")
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "calculate" in user_input:
        try:
            result = eval(user_input.replace("calculate", "").strip())
            speak(f"The result is {result}")
        except:
            speak("Sorry, I am unable to calculate that right now")
    else:
        speak("I didn't understand that. Can you try again?")