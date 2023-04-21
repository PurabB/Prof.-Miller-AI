# !pip install SpeechRecognition
# !pip install openai
# !pip install gTTS
# !pip install pyaudio
# installed libraries

import speech_recognition as sr
import openai
import os
from gtts import gTTS
import pyttsx3
import pyaudio
import wave

OPENAI_API_KEY = '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'#openAI key
openai.api_key = OPENAI_API_KEY

r = sr.Recognizer() #recognizer object
keyWord = 'jarvis'
with sr.Microphone() as source: #microphone is source of audio recognizer
    print("Listening: ")
    audio = r.listen(source)

r = sr.Recognizer()
keyWord = 'jarvis'
with sr.Microphone() as source:
    print('Please start speaking..\n')
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

def generate_response(prompt): #a function set to generate a response from gpt-3
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

response = generate_response(text) #print response as text arguement in command line
print(response)

tts = gTTS(response) #converts the response text to audio file
tts.save("response.mp3")
os.system("response.mp3") #plays the audio file

# def text_to_speech(response):
#     #engine connects us to hardware in this case 
#     eng = pyttsx3.init()
#     #Engine created 
#     eng.say(response)
#     #Runs for small duration of time ohterwise we may not be able to hear
#     eng.runAndWait()

# def main():
#     #

# if __name__ == "__main__":
#     main()



# audio = pyaudio.PyAudio() #initialize a PyAudio object
# input_device_index = None
# for i in range(audio.get_device_count()): #search for mic in range
#     device_info = audio.get_device_info_by_index(i)
#     if device_info["name"].lower() == "microphone":
#         input_device_index = device_info["index"]
#         break
# if input_device_index is None: #return error if no microphone
#     raise ValueError("No microphone was found")
# stream = audio.open( # Set the microphone as the audio source
#     format=pyaudio.paInt16,
#     channels=1,
#     rate=44100,
#     input=True,
#     input_device_index=input_device_index,
# )

# wavefile = wave.open("recording.wav", "wb") #create wave object
# wavefile.setnchannels(1)
# wavefile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
# wavefile.setframerate(44100)
# # Read audio from the microphone and save it to the file
# data = stream.read(1024)
# while data:
#     wavefile.writeframes(data)
#     data = stream.read(1024)
# wavefile.close()
# stream.stop_stream()
# stream.close()
# audio.terminate()





