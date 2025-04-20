import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import subprocess
import datetime
# import google.generativeai as genai

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("J.A.R.V.I.S. : Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        print("J.A.R.V.I.S. : I am Listening...")
        audio = recognizer.listen(source)
        try:
            print("J.A.R.V.I.S. : Recognizing your commands...")
            text = recognizer.recognize_google(audio)
            print(f"you : {text}")
            return(text)
        except Exception as e:
            print(f"J.A.R.V.I.S. : Sorry, I could not recognize that command.")
            return "Sorry, I could not recognize that command."

def generativeAI_response(prompt):
    try:
        prompt = "".join(prompt.split("intelligence")[1:]).strip()
        genai.configure(api_key = "use your Api-key")    
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 2000,
        "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
        )
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(prompt)
        res = response.text
        if not os.path.exists("OpenAI_Response"):
            os.mkdir("OpenAI_Response")
        with open(f"OpenAI_Response/res-{prompt}.txt", "w") as f: 
            f.write(res)
        res = res[:500] + f"<<--for more information read the document which named in your prompt dot t x t-->>"
        return res
    except Exception as e:
        print(f"J.A.R.V.I.S. : Sorry, I could not get any response from my server.")
        return "Sorry, I could not get any response from my server."


if __name__ == '__main__':
    text_to_speech("Hellow i am Jarvis AI")
    lists = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"], ["chat GPT", "https://chatgpt.com"], ["translator", "https://www.google.com/search?q=translate+in+bengali&rlz=1C1UEAD_enIN999IN999&oq=tran&aqs=chrome.0.35i39j69i57j35i39j0i131i433i512j0i512j0i131i433i512j0i433i512j5.2084j0j7&sourceid=chrome&ie=UTF-8"]]
    apps = [["notepad", "notepad.exe"], ["paint", "mspaint.exe"], ["calculator","calc.exe"], ["settings","ms-settings:"], ["photos","ms-photos:"], ["clock","ms-clock:"]]
    while True:
        query = speech_to_text()
        if "ok jarvis shut down".lower() in query.lower():
            text_to_speech("Ok then bye. Have a Good day")
            break
        if f"open".lower() in query.lower() :
            for list in lists:
                if f"open {list[0]}".lower() in query.lower():
                    webbrowser.open(f"{list[1]}")
                    text_to_speech(f"Opening {list[0]}")
            for app in apps:
                if f"open {app[0]} application".lower() in query.lower():
                    os.startfile(f"{app[1]}")
                    text_to_speech(f"Opening {app[0]} application")
        if f"play music".lower() in query.lower():
            # Path to your audio file
            audio_file = "F:\Jarvis_AI\Wiz_Khalifa.mp3"
            text_to_speech("Opening music")
            # Command to open the file with Windows Media Player
            subprocess.run(["start", "wmplayer", audio_file], shell=True)
        if f"what's the time it is".lower() in query.lower():
            now = datetime.datetime.now() # Get the current date and time
            day = now.strftime("%A") # Format the date and time
            date = now.strftime("%Y/%m/%d")
            time = now.strftime("%H:%M:%S")
            today = f"Today : {day}, Date : {date}, Time : {time}"
            print(f"{today}")
            text_to_speech(f"{today}")
        # if f"using artificial intelligence".lower() in query.lower():
        #     res = generativeAI_response(query)
        #     text_to_speech(res)