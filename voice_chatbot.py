import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Speak something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."
    except sr.RequestError:
        return "Error with the speech recognition service."

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am a voice chatbot."
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def main():
    print("🤖 Voice Chatbot is running. Say something!")
    while True:
        user_input = listen_to_user()
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("🤖 Bot:", get_bot_response(user_input))
            break
        print("🤖 Bot:", get_bot_response(user_input))

if __name__ == "__main__":
    main()
