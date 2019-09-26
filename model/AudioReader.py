from threading import Thread, Lock, Event
import pyaudio
import numpy as np
import time
import wave
from collections import deque

class ThreadMicrophone(Thread):
    def __init__(self, rate=44100):
        Thread.__init__(self)
        self.chunksize = int(rate*0.05) # 50ms
        self.background_energy = []
        self.energy = deque(maxlen=int(rate*0.1)) # 100ms
        self.rate = rate
        self.p = pyaudio.PyAudio()
        self.default_info = self.p.get_default_input_device_info()
        self.channels = 1
        self.stream = self.p.open(format=pyaudio.paInt16,channels=self.channels,rate=rate,
                                  input=True)

        self.data = []
        self.speaker_present = False
        self.idle_counter = 0
        self.event = Event()
        self.kill_event = Event()
        self.lock = Lock()
        self.config = {'sample_width': self.p.get_sample_size(pyaudio.paInt16),
                  'rate':self.rate,
                  'channels':self.channels
                  }


    def get_bytes(self):
        r = []
        if self.event.is_set():
            with self.lock:
                print('Reading')
                r, self.data[:] = self.data[:], []
                self.event.clear()
        return r


    def background_noise(self):
        print('Recording Background Noise')
        # Start with collecting background noise for 5 seconds
        for i in range(0, int(self.rate / self.chunksize * 5)):
            chunk = np.fromstring(self.stream.read(self.chunksize), dtype=np.int16)
            energy = np.linalg.norm(chunk, axis=0) ** 2
            self.background_energy.append(energy)

        print('Done with background noise')

    def run(self):
        if self.background_energy:
            while True:
                time.sleep(0.000001)
                # If we need to stop
                if not self.kill_event.is_set():
                    # If a recording is ready dont do it
                    if not self.event.is_set():
                        with self.lock:
                            chunk_string = self.stream.read(self.chunksize)
                            chunk = np.fromstring(chunk_string,dtype=np.int16)
                            energy = np.linalg.norm(chunk, axis=0) ** 2
                            self.energy.append(energy)
                            # Is a speaker present
                            if energy > (np.mean(self.background_energy)+np.std(self.background_energy)):
                                self.idle_counter = 0
                                self.speaker_present = True
                                print('I hear you')
                            else:
                                self.idle_counter += 1

                            # Has the speaker ended
                            if (self.idle_counter > 0) & ((self.idle_counter % 10) == 0) & (self.speaker_present):
                                self.speaker_present = False
                                print('Speak Ended')
                                self.event.set()
                            # Append data if speaker is talking
                            if self.speaker_present:
                                self.data.append({'data_string':chunk_string,'data':chunk})

                else:
                    print('Breaking')
                    # Clean up
                    self.stream.stop_stream()
                    self.stream.close()
                    self.p.terminate()
                    break

        else:
            print('Calculate background noise first')

    def stop(self):
        self.kill_event.set()



def save_aud(aud_string, filename, t):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(t.p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(t.rate)
    wf.writeframes(b''.join(aud_string))
    wf.close()

'''
import pyaudio
import wave
import numpy as np
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "outputnew.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    print(data)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()


wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()




from AudioReader import ThreadMicrophone
import time
from scipy.fftpack import fft

t = ThreadMicrophone()
t.start()
for i in range(10):
    chunk = t.get_bytes()
    
    


import pyaudio
import wave
import numpy as np
from scipy.fftpack import fft
from sklearn.preprocessing import StandardScaler
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = RATE*3
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "outputnew.wav"
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("* recording")
frames = []
frames_ = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data_ = np.fromstring(data, dtype=np.int16)
    chunk = data_
    X = np.abs(fft(chunk))
    frames_.append(X)
    frames.append(data)
print("* done recording")
import time
print("no sound!!")
time.sleep(1)
print("* recording")
frames_no_sound = []
frames_no_sound_ = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data_ = np.fromstring(data, dtype=np.int16)
    chunk = data_
    X = np.abs(fft(chunk))
    frames_no_sound_.append(X)
    frames_no_sound.append(data)
print("* done recording")
stream.stop_stream()
stream.close()
p.terminate()
    
    



    
    
for a in frames_:
    print('\n \n \n \n')
    plt.plot(a)
    plt.show()
    chunk = a
    print(f'energy {np.linalg.norm(chunk,axis=0)**2}')
    X = np.abs(fft(chunk))
    SFM = np.exp(np.log(X).mean()) / (np.mean(X))
    print(SFM)
    print(np.sum(X))
print('switching to no sound')
for b in frames_no_sound_:
    print('\n \n \n \n')
    plt.plot(b)
    plt.show()
    chunk = b
    print(f'energy {np.linalg.norm(chunk, axis=0) ** 2}')
    X = np.abs(fft(chunk))
    SFM = np.exp(np.log(X).mean()) / (np.mean(X))
    print(SFM)
    print(np.sum(X))
    
'''