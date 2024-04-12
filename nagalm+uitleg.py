from scipy.signal import find_peaks
from scipy.signal import savgol_filter
import time
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# hier geef je aan hoeveel stoelen en rijen je hebt, ook hoeveel meetingen je per stoel wilt doen
# als je een andere soort ruimte gaat meeten voor je hier in hoeveel meetingen je in de lengte en breete doet
# hier geef je aan hoegrote drop van db je wilt meten en hij berekend meteen de factor die je nagalm tijd vermedigd vuldigd zodat hij een werkelijke drop van 60 zou hebben
stoelen = 7
rijen = 2
tests = 3
aantal_meetingen_perstoel = 3
db_drop = 20
factor  = 60/db_drop
# hier maak je een lijst met waardes voor het verkrijgen van de juiste waardes op de assen van de heatmap
stoel_nummers = np.arange(1,stoelen + 1,1)
rij_nummers   = np.arange(1,rijen + 1,1)


# hier maak je een lijstr aan waar alle nagalmtijden in komen te staan
nagalmtijden = []
# hier zorg je ervoor dat python de files uit een geselecteerde map haalt dit moet je zelf aanpassen voor waar jou bestanden worden opgeslagen
folder_path = '/Users/vincentroestenburg/Documents/project1.3/codemicrofoon/wav/'

# hier maak je een lijst aan met in die lijst het aantal stoelen word zo weergegeven s1 , s2 ..
def stoelen_lijst():
    lijst = []
    for s in range(1,stoelen+1):
        x = f's{s}'
        lijst.append(x)
    return lijst

# hier maak je een lijst aan met in die lijst het aantal rijen word zo weergegeven r1, r2, ..
def rijen_lijst():
    lijst = []
    for s in range(1,rijen+1):
        x = f'r{s}'
        lijst.append(x)
    return lijst

# hier maak je een lijst aan met in die lijst het aantal testen dat je doet word zo weergeven t1, t2, ..
def test_lijst():
    lijst = []
    for s in range(1,tests+1):
        x = f't{s}'
        lijst.append(x)
    return lijst

# hier is een loop die per rij dan per stoel en dan per test de code hieronder doet
for rij in rijen_lijst():
    for stoel in stoelen_lijst():
        for test in test_lijst():
            # hier laad je de bestanden in hij doet dit alsvolgt hij pakt eerst de eerste rij uit de lijst rijen dan de eerste stoel dan de eerste test en zo gaat hij door het aantal gekozen test per stoel en zo werkt hij alle stoelen en rijen af
            y, rs = librosa.load(f'{folder_path}{rij}-{stoel}-{test}.wav', sr=None)
            # hier neem je de absolute waarde va de data zodat je geen negatieve getallen krijgt
            S = np.abs(y)
            # hier berekend hij de db vanuit de data
            db = librosa.amplitude_to_db(S, ref=1)
            # hier doet hij + 80 db
            db += 80
            # hier smoothe je de db dat beteknd dat we er een filter over hebben gezged deze filter word uitgelegd in ons verslag
            smoothed_db = savgol_filter(db, window_length=4411, polyorder=4)
            # hier zorg je ervoor dat inder elk punt van de data een tijd komt te staan zodat je de nagalmtijd makkeljk kan berekenen
            time = np.arange(0, len(db)) / rs

            # hier zoek hij de maximale waarde van de data dit is dus waneer de nagalm tijd begint
            max_waarde = np.max(smoothed_db)
           
            piek = np.argmax(smoothed_db)
           
            search_range = slice(piek, None)
            # hier =geeft hij aan welke index staat oinder de plek waar de top - drop is dus wanner hij een bepaald aantal db is gedropt
            index_below_threshold = np.where(smoothed_db[search_range] <= (max_waarde - db_drop))[0][0]
            # hier geeft hij de tijd van waar hij zoveel db is gedrop
            time_below_threshold = time[piek + index_below_threshold]
            # hier geeft hij aan wat de tijd onder de piek is
            time_below_max = time[piek]
            # hier berekend hij de nagalm tijd door de twee tijden van elkaar afte halen en met berekende factor te vermedig vuldigen
            nagalmtijden.append((time_below_threshold - time_below_max)*factor)
           
# hier maak je een array van de lijst net nagelmtijden
arr = np.array(nagalmtijden)
# hier vervormd hij de array naar een array die bestaand uit een lijst van de eerste 3 getallen en daaronder de tweede 3 enzovoort
reshaped_arr = arr.reshape(-1, aantal_meetingen_perstoel)
# hier worden alle gemiddelde nagalmtijden berekend door van elke 3 meetingen de gemmiddelde te nemen
gemiddelden = np.mean(reshaped_arr, axis=1)

# hier vervorm je de lijst met gemiddelde nagalmtijden tot een aray die bestaad uit dezelfde vorm als je college zaal door het in evenveel rijen en stoelen te plaatsen dit word automatisch op de goede volgorde gedaan
data_array = np.array(gemiddelden).reshape(rijen, stoelen)

# hier geef je de namen van de rijen en colommen
rij_namen = ['rij{}'.format(i+1) for i in range(rijen)]
colom_namen = ['stoel{}'.format(j+1) for j in range(stoelen)]  

# hier maak je van de array een dataframe die noem je df dit doe je zodat je makkelijk een heatmap kunt maken met seaborn
df = pd.DataFrame(data_array, columns=colom_namen, index=rij_namen)

# hier maak je de heatmap met seaborn je kies de kleur en geeft een label
sns.heatmap(data, annot=True, cmap='BuRd', fmt='.2f', cbar_kws={'label': 'Nagalmtijden'})

# hier geef je de heatmap een titel en zorg je ervoor dat de goede waardes op de assen staan
plt.title('Heatmap WBH02B09 -- Projectgroep 4')
plt.xticks(np.arange(stoelen), stoel_nummers)
plt.yticks(np.arange(rijen), rij_nummers)
plt.xlabel('Stoel')
plt.ylabel('Rij')
