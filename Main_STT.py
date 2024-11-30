#############################################
#### Python Azure Speech-to-Text Program ####
#############################################

# Libraries
import azure.cognitiveservices.speech as azuresystem
from azure.cognitiveservices.speech import AudioConfig
from azure.cognitiveservices.speech import ResultReason
import thread
from pynput import keyboard
import time

# Recognizer Events:
def recognized_handler(source, event_args):
    global final_text
    print(f'Recognized ({source}): {event_args.result.text}')
    final_text = event_args.result.text

def recognizing_handler(source, event_args):
    print(f'Recognizing ({source}): {event_args.result.text}')

def cancelation_handler(source, event_args):
    print(f'Canceled ({source}): {event_args.reason}')
    if event_args.reason == azuresystem.CancellationReason.Error:
        print(f"Error: {event_args.error_details}")

# Thread & Pynput listener Combo for mic_recorder:
mic_thread_running = False

def mic_recorder():
    # Setup
    talking_stick = "api_key"
    service_region = 'region'
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
# mic_input = thread.Thread(target=mic_recorder)   

# Call
# print('Press Spacebar')
# with keyboard.Listener(on_press=spacebar_checker) as listener:
#    listener.join()

final_text = ''
talking_stick = "api_key"
service_region = 'region'
audio_config = AudioConfig(use_default_microphone=True)
speech_config = azuresystem.SpeechConfig(subscription=talking_stick, region=service_region)
speech_config.speech_recognition_language = 'en-US'
recognizer = azuresystem.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

recognizer.recognized = recognized_handler
recognizer.recognizing = recognizing_handler
recognizer.canceled = cancelation_handler

print("You're Live!!!!")
recognizer.start_continuous_recognition
value = input('Press enter: ')
print('Mic Drop!!!!') 
recognizer.start_continuous_recognition 
print(f'{final_text}')