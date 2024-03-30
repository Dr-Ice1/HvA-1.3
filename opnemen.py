# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:48:08 2024

@author: thijs
"""
#imports
import pyaudio
import wave
import time

#audio bestand specs
Chunk=1024
Format = pyaudio.paInt16
Rate = 44100
seconds = 2.2

#geeft aan via welke channel je opneemt zorg dat je weet welk getal de microfoon is
Channels = 1


#zet opnamen om in wav file. Let op dat de file overgeschreven wordt als de file naam niet veranderd.

per_stoel = ['t1', 't2', 't3']
tijd_tussen_metingen = .4

stoel = 17

rij = 8

for test in per_stoel:
    #start opnamen
    p = pyaudio.PyAudio( )
    stream = p.open(format=Format,
            channels=Channels,
            rate=Rate,
            input=True,
            frames_per_buffer=Chunk)
    print(f'Opname: r{rij}-s{stoel}-{test}.wav')
    print("start opnemen")
    frames = []
    for i in range(0,int(Rate/Chunk*seconds)):
        data = stream.read(Chunk)
        frames.append(data)
    print("opnemen gestopt")
    print('')
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(f"r{rij}-s{stoel}-{test}.wav", 'wb')
    wf.setnchannels(Channels)
    wf.setsampwidth(p.get_sample_size(Format))
    wf.setframerate(Rate)
    wf.writeframes(b''.join(frames))
    wf.close
    time.sleep(tijd_tussen_metingen)