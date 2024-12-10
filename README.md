# Speech-to-Text
Azure Text to Speech Program:

Currently this system utilizes the following libraries:
azure.cognitiveservices.speech
azure.cognitiveservices.speech, AudioConfig
thread
pynput, keyboard
time
os

To set up correctly, you will need to export your api_key and region as env variavles in the relevant output terminal. Looks like this;
export api_key='your_actual_key'
export region='your_actual_region'
For this program I used the os library to call the env variables, however this isn't essential.

The program is designed to listen for the spacebar as a prompt to both start and end the STT process. You can change this in the spacebar_checker function by utilizing relevant pynput library code.

Using the recognizing event handler, it will also constantly update you on any word it hears. If you'd like to disable this I recommend deleting the recognizing_handler caller from the mic_recorder func. It is unnessential and will not break anything upon removal (or at least it shouldn't).
