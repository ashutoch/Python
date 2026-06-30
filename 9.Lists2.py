
#! Python AI assitant

#? Import necessary libraries
import pyttsx3
from datetime import datetime

#? Initialize the text to speech engine
# engine = pyttsx3.init()

#? Define a function to speak text
def speak(text):
    print("AI Bot:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine 


#? Greet someone 
print("Jarvis: Hello! I am a python ai assistant bot... Type 'exit' to end\n")


#? Start the chat loop
while True:
    user_input = input("👤You: ").lower()


    if user_input == 'exit':
        speak("Hope i was able to help")
        break


#? If user says hello or hi, the bot replies
    elif "hello" in user_input or "hi" in user_input:
        speak("Hello! I am Jarvis, how may i assist you today?")


#? How are you
    elif "how are you" in user_input:
        speak("I am just a bot! I don't feel the emotions so i am unable to answer your query...")


#? Name
    elif "name" in user_input:
        speak("My name is Jarvis")


#? Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(current_time)


#? Calculate
    elif "calculate" in user_input:
        try:
            result = eval(user_input.replace("calculate", ""))
            speak(f"The result is: {result}")
        except:
            speak("Sorry i am unable to calculate that right now")


    else:
        speak("I didn't understand that. Can you try again?")