# -- coding: utf-8 --
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
# hier geef je aan wat de tijd tussen de opeenvolgende meetingen zijn
tijd_tussen_metingen = .4
# hier zet je de stoelnummer
stoel = 17
# hier zet je de rijnummer
rij = 8
# hier runt hij alle code in deze loop voor test 1 ,2 en 3 zo neemt hij dus 3 keer op en de tijd tussen elke opname kan je in de eerde vertelde lijn invoeren
for test in per_stoel:
    #start opnamen
    p = pyaudio.PyAudio( )
    stream = p.open(format=Format,
            channels=Channels,
            rate=Rate,
            input=True,
            frames_per_buffer=Chunk)
    # hier print je welke stoel en welke test je doet zodat jij weet welke test het is
    print(f'Opname: r{rij}-s{stoel}-{test}.wav')
    # hier word start opname geprint zodat jij weet nu is de microfoon aan het opnemen en nu moeten we ons geluid maken 
    print("start opnemen")
    frames = []
    for i in range(0,int(Rate/Chunk*seconds)):
        data = stream.read(Chunk)
        frames.append(data)
    # hier print je opname gestopt zodat jij weet dat de opname voorbij is pas wel op dat er automatisch 3 opnames achterelkaar gaan met een korte tussen tijd bij elk van de drie opnames word geprint start en stop  
    print("opnemen gestopt")
    print('')
    # hier word de opname gestop en zorgt de code dat de microfoon niks meer opneemt 
    stream.stop_stream()
    stream.close()
    p.terminate()
    # hier word een wav file aangemaakt om de opgenomen audio in op te slaan 
    wf = wave.open(f"r{rij}-s{stoel}-{test}.wav", 'wb')
    # hier word het audio kanaal gekozen deze worden bepaald door een eerder beschreven variable die wij zelf kunnen aanpassen
    wf.setnchannels(Channels)
    # hier geef je de sampel size aan sampel size heeft te maken met hoe nauwkeurig de meeting is hoe breeder hoe nauwkeuriger de data is 
    wf.setsampwidth(p.get_sample_size(Format))
    wf.setframerate(Rate)
    # hier word alle dat ain het wav bestand gezet 
    wf.writeframes(b''.join(frames))
    # hier word het bestand gesloten zodat er geen extra nonodige data in het bestand terecht zou kunnen komen 
    wf.close
    # hier word de tijd tussen de meetingen bepaald door de eerder benoemde zelf te verandere variabelen
    time.sleep(tijd_tussen_metingen)