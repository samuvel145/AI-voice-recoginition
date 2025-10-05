import speech_recognition as sr
import pyttsx3
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that. Please type your request.")
        typed = input("Type your request: ")
        if typed.strip():
            return typed.strip()
        return None
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        speak("Could not request results; check your network connection.")
        return None

def ai_response(prompt):
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"Error: {e}")
        speak("There was an error with the AI service.")
        return "Error with AI service."

def main():
    print("Voice Assistant is running. Say something!")
    while True:
        query = listen()
        if query:
            answer = ai_response(query)
            print(f"Assistant: {answer}")
            speak(answer)

if __name__ == "__main__":
    main()
