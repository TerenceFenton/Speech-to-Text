# Python Mic Audio Input

# Dependencies
import pyaudio
import wave

# Audio Parameters
chunkk = 1024
formatt = pyaudio.paInt16
channelss = 1
ratee = 44100

# PyAudio Instance
instance = pyaudio.PyAudio()

stream = instance.open(format=formatt, channels=channelss, rate=ratee, input=True, frames_per_buffer=chunkk)

# Recorder Func
def voice_recorder(chunkk, ratee):
    frames = []
    seconds = 3
    for i in range(0, int(ratee / chunkk * seconds)):
        data = stream.read(chunkk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    return frames

# Save File Func
def save_file(channelss, formatt, ratee, frames, instance):
    prompt = input(f'Save File? (Y/N): ')
    real_inputs = ['Y', 'N', 'y', 'n']

    while prompt not in real_inputs:
        print('Please only answer Y or N')
        prompt = input(f'Save File? (Y/N): ')
    
    if prompt == 'Y' or prompt == 'y':
        wf = wave.open("output.wav", 'wb')
        wf.setnchannels(channelss)
        wf.setsampwidth(instance.get_sample_size(formatt))
        wf.setframerate(ratee)
        wf.writeframes(b''.join(frames))
        wf.close()

# Interactive Func
def interactive_experience(instance, chunkk, formatt, channelss, ratee):
    prompt = input(f'Start Recording? (Y/N): ')
    real_inputs = ['Y', 'N', 'y', 'n']

    while prompt not in real_inputs:
        print('Please only answer Y or N')
        prompt = input(f'Start Recording? (Y/N): ')
    
    if prompt == 'Y' or prompt == 'y':
        print('Recording Sample')
        frames = voice_recorder(chunkk, ratee)
        print('Recording Complete')
        instance.terminate()
        save_file(instance, frames, formatt, channelss, ratee)

    print('Have a great day')



