# !pip install SpeechRecognition
# !pip install openai
# !pip install gTTS
# !pip install pyaudio
# !pip install pyttsx3
# installed libraries

# import os
# from gtts import gTTS
# import pyaudio
# import wave

import speech_recognition as sr
import openai
import pyttsx3
import time

# def myListen(self,x):
#     return

def main():
    OPENAI_API_KEY = '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'#openAI key
    openai.api_key = OPENAI_API_KEY

    t0 = time.time()
    r = sr.Recognizer() #recognizer object
    #print("took", time.time()-t0)
    keyWord = 'Professor Miller'
    #t0 = time.time()
    with sr.Microphone() as source: #microphone is source of audio recognizer
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Starting up... ")
        # r.listen = myListen
        audio = r.listen(source)
    
    r = sr.Recognizer()
    keyWord = 'Professor Miller'
    with sr.Microphone() as source:
        print('Ask me a qustion! \n')
        while True: 
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                if keyWord.lower() in text.lower():
                    print('Keyword detected in the speech.')
                    break
            except Exception as e:
                print('Please speak again.')

    text = r.recognize_google(audio) #convert audio to text
    print(text)

    response = generate_response(text) #print response as text arguement in command line
    print(response)

    # tts = gTTS(response) #converts the response text to audio file
    # tts.save("response.mp3")
    # os.system("response.mp3") #plays the audio file

    tts =  text_to_speech(response)

def generate_response(prompt): #a function set to generate a response from gpt-3
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

def text_to_speech(response):
    #engine connects us to hardware in this case 
    eng = pyttsx3.init()
    #Engine created 
    eng.say(response)
    #Runs for small duration of time ohterwise we may not be able to hear
    eng.runAndWait()

if __name__ == "__main__":
    while True:
        main()




