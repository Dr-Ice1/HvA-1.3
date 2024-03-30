import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import seaborn as sns



stoelen = 17
rijen = 8
aantal_meetingen_perstoel = 3


nagalmtijden = []
folder_path = 'C:/Users/alexa/Documents/Git/Blok3/Mic/wav/'


def stoelen_lijst():
    lijst = []
    for s in range(1,stoelen+1):
        x = f's{s}'
        lijst.append(x)
    return lijst

def rijen_lijst():
    lijst = []
    for s in range(1,rijen+1):
        x = f'r{s}'
        lijst.append(x)
    return lijst

def test_lijst():
    lijst = []
    for s in range(1,aantal_meetingen_perstoel+1):
        x = f't{s}'
        lijst.append(x)
    return lijst


for rij in rijen_lijst():
    for stoel in stoelen_lijst():
        for test in test_lijst():
            y, rs = librosa.load(f'{folder_path}{rij}-{stoel}-{test}.wav', sr=None)
            S = np.abs(y)
            db = librosa.amplitude_to_db(S, ref=1)
            db += 80
            smoothed_db = savgol_filter(db, window_length=4411, polyorder=4)
            time = np.arange(0, len(db)) / rs

            max_waarde = np.max(smoothed_db)
            piek = np.argmax(smoothed_db)
            search_range = slice(piek, None)
            index_below_threshold = np.where(smoothed_db[search_range] <= (max_waarde - 20))[0][0]
            time_below_threshold = time[piek + index_below_threshold]
            time_below_max = time[piek]
            nagalmtijden.append((time_below_threshold - time_below_max)*3)
arr = np.array(nagalmtijden)
reshaped_arr = arr.reshape(-1, aantal_meetingen_perstoel)
gemiddelden = np.mean(reshaped_arr, axis=1)

print(f'Nagalmtijden per stoel: {gemiddelden}')


### Heatmap - datavisualisatie
reshaped_arr = np.reshape(np.array(gemiddelden), (-1, stoelen))
data = reshaped_arr
print(data)

sns.heatmap(data, annot=True, cmap='viridis', fmt='.2f', cbar_kws={'label': 'Nagalmtijden'})

plt.title('Heatmap WBH02B09 -- Projectgroep 4')
plt.xlabel('Stoel')
plt.ylabel('Rij')

plt.xticks(np.arange(0.5, data.shape[1]+0.5, 1), np.arange(1, data.shape[1]+1, 1))
plt.yticks(np.arange(0.5, data.shape[0]+0.5, 1), np.arange(1, data.shape[0]+1, 1))

plt.show()

