# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:48:08 2024

@author: thijs
"""
#imports
import pyaudio
import wave

#audio bestand specs
Chunk=1024
Format = pyaudio.paInt16
Rate = 44100
seconds = 2.2

#geeft aan via welke channel je opneemt zorg dat je weet welk getal de microfoon is
Channels = 1


#zet opnamen om in wav file. Let op dat de file overgeschreven wordt als de file naam niet veranderd.


#start opnamen
p = pyaudio.PyAudio( )
stream = p.open(format=Format,
        channels=Channels,
        rate=Rate,
        input=True,
        frames_per_buffer=Chunk)
print("start opnemen")
frames = []
for i in range(0,int(Rate/Chunk*seconds)):
    data = stream.read(Chunk)
    frames.append(data)
print("opnemen gestopt")
stream.stop_stream()
stream.close()
p.terminate()
wf = wave.open("80db-10000hz.wav", 'wb')
wf.setnchannels(Channels)
wf.setsampwidth(p.get_sample_size(Format))
wf.setframerate(Rate)
wf.writeframes(b''.join(frames))
wf.close