# Python Mic Audio Input

# Dependencies
import pyaudio
import wave

# Audio Parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# PyAudio Instance
instance = pyaudio.PyAudio()

stream = instance.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Recorder Func
def voice_recorder(CHUNK, RATE):
    frames = []
    seconds = 3
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    instance.terminate()
    return frames

# Save File Func
def save_file(FRAMES):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    instance = pyaudio.PyAudio()
    prompt = input(f'Save File? (Y/N): ')
    real_inputs = ['Y', 'N', 'y', 'n']

    while prompt not in real_inputs:
        print('Please only answer Y or N')
        prompt = input(f'Save File? (Y/N): ')
    
    if prompt == 'Y' or prompt == 'y':
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(instance.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(FRAMES))
        wf.close()

# Interactive Func
def interactive_experience(instance, CHUNK, FORMAT, CHANNELS, RATE):
    prompt = input(f'Start Recording? (Y/N): ')
    real_inputs = ['Y', 'N', 'y', 'n']

    while prompt not in real_inputs:
        print('Please only answer Y or N')
        prompt = input(f'Start Recording? (Y/N): ')
    
    if prompt == 'Y' or prompt == 'y':
        print('Recording Sample')
        frames = voice_recorder(CHUNK, RATE)
        print('Recording Complete')
        save_file(frames)

    print('Have a great day')

# Main
interactive_experience(instance, CHUNK, FORMAT, CHANNELS, RATE)

