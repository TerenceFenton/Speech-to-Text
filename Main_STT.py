#############################################
#### Python Azure Speech-to-Text Program ####
#############################################

# Libraries
import azure.cognitiveservices.speech as azuresystem
from azure.cognitiveservices.speech import AudioConfig
import thread
from pynput import keyboard
import time
import os

# Recognizer Events:
def recognized_handler(event_args):
    global final_text
    print(f'Recognized: {event_args.result.text}')
    final_text = event_args.result.text

def recognizing_handler(event_args):
    global final_text
    print(f'Recognizing: {event_args.result.text}')

def cancelation_handler(event_args):
    print(f'Canceled: {event_args.reason}')
    if event_args.reason == azuresystem.CancellationReason.Error:
        print(f"Error: {event_args.error_details}")

# Thread & Pynput listener Combo for mic_recorder:
mic_thread_running = False
final_text = ''

def mic_recorder():
    # Setup
    global final_text
    talking_stick = os.getenv('API_KEY')
    service_region = os.getenv('REGION')
    audio_config = AudioConfig(use_default_microphone=True)
    speech_config = azuresystem.SpeechConfig(subscription=talking_stick, region=service_region)
    speech_config.speech_recognition_language = 'en-US'
    recognizer = azuresystem.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Attach Recognition Events
    recognizer.recognized.connect(recognized_handler)
    recognizer.recognizing.connect(recognizing_handler)
    recognizer.canceled.connect(cancelation_handler)
      
    # Process  
    global mic_thread_running
    print('You are live!')
    recognizer.start_continuous_recognition()   
    try:
        while mic_thread_running:
            time.sleep(1)
    finally:
        recognizer.stop_continuous_recognition()
        print('Mic Drop!!!')
        print(f'{final_text}')



def spacebar_checker(key):
    global mic_thread_running  
    if key == keyboard.Key.space:
        if mic_thread_running is False:
            mic_thread_running = True 
            mic_input.start() 
        else:
            mic_thread_running = False
            mic_input.join() 
            return False    

# Thread
mic_input = thread.Thread(target=mic_recorder)   

# Call
print('Press Spacebar')
with keyboard.Listener(on_press=spacebar_checker) as listener:
    listener.join()