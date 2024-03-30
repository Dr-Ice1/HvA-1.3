import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

x = ['Lage intensiteit', 'Middel intensiteit', 'Hoog intensiteit']

hz200_meter = [49.5, 70, 71.4]
hz200_mic = [48, 73, 73]
hz200_delta = [1.5,-3,-1.6]

hz10k_meter = [53,70,78.8]
hz10k_mic = [51.7,66.9,77.8]
hz10k_delta = [1.3,3.1,1]


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)

### 500 Hz grafiek  ###
hz500_meter = [49.8, 69.8, 79.9]
hz500_mic = [45.1, 64.1, 75.3]
hz500_delta = [4.7,5.7,4.6]
#plot, title, legend, text
ax1.plot(x, hz500_meter, c='orange', label='dB-meter')
ax1.plot(x, hz500_mic, label='dB-mic', c='b')
ax1.set_title('$f$ = $500$ Hz')
ax1.legend(loc='center left', bbox_to_anchor=(.99, 0.5))
ax1.text(0,80,'$\Delta_{gem} = 5$',bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8)))
#annotate delta 1
# ax1.annotate('', xy=(0, 45), xytext=(0, 50),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax1.annotate('$\Delta = 4.7$', xy=(0, 52), xytext=(-.02, 65),arrowprops=dict(facecolor='black', arrowstyle='->'))
#annotate delta 2
# ax1.annotate('', xy=(1, 64.1), xytext=(1, 69.9),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax1.text(1.04,67.5,'$\Delta = 5.7$')
#annotate delta 3
# ax1.annotate('', xy=(2, 75.3), xytext=(2, 79.9),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax1.text(1.77,76,'$\Delta = 4.6$')
# errorbars
ax1.errorbar(x, hz500_mic, yerr=[2, 1, 1.3], capsize=5)


### 1000Hz  ###
hz1000_meter = [56.7, 70.7, 79.9]
hz1000_mic = [46.3, 60.6, 69.1]
hz1000_delta = [10.4,10.1,10.8]
#plot, title, text
ax2.plot(x, hz1000_meter, c='orange')
ax2.plot(x, hz1000_mic, c='b')
ax2.set_title('$f$ = $1000$ Hz')
ax2.text(0,80,'$\Delta_{gem} = 10.4333$',bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8)))
#annotates
# ax2.annotate('', xy=(0, 46.1), xytext=(0, 56.7),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax2.text(0.05,53,'$\Delta = 10.4$')

# ax2.annotate('', xy=(1, 60.6), xytext=(1, 70.7),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax2.text(1.05,65,'$\Delta = 10.1$')

# ax2.annotate('', xy=(2, 69.1), xytext=(2, 79.9),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax2.text(1.74,72,'$\Delta = 10.8$')
### Errorbar
ax2.errorbar(x, hz1000_mic, yerr=[2.3, 2, 2.7], capsize=5)

###    3kHz    ###
hz3000_meter = [58.1,71.3,83.9]
hz3000_mic = [47.5,60.6,72.9]
hz3000_delta = [10.6,10.7,11]
#plot, title, legend, text
ax3.plot(x, hz3000_meter, c='orange', label='dB-meter')
ax3.plot(x, hz3000_mic, label='dB-mic', c='b')
ax3.set_title('$f$ = $3000$ Hz')
ax3.legend(loc='center left', bbox_to_anchor=(.99, 0.5))
ax3.text(0,80,'$\Delta_{gem} = 10.767$',bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8)))
#annotate + text
# ax3.annotate('', xy=(0, 47.5), xytext=(0, 58.1),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax3.text(0.05,54,'$\Delta = 10.6$')

# ax3.annotate('', xy=(1, 60.6), xytext=(1, 71.3),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax3.text(1.05,67,'$\Delta = 10.7$')

# ax3.annotate('', xy=(2, 72.9), xytext=(2, 83.9),arrowprops=dict(facecolor='black', arrowstyle='<->'))
ax3.text(1.7,75,'$\Delta = 10.4$')
# error
ax3.errorbar(x, hz3000_mic, yerr=[4.3, 4, 4.7], capsize=5)

###     5kHz    ###
hz5000_meter = [49.5,70.5,79.2]
hz5000_mic = [49,69.3,78.5]
hz5000_delta = [.5,1.2,.7]
#plot, title, text
ax4.plot(x, hz5000_meter, c='orange')
ax4.plot(x, hz5000_mic, c='b')
ax4.set_title('$f$ = $5000$ Hz')
ax4.text(0,80,'$\Delta_{gem} = 0.8$',bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8)))
#annotate
ax4.annotate('$\Delta = 0.5$', xy=(0, 50), xytext=(0, 56),arrowprops=dict(facecolor='black', arrowstyle='->'))
ax4.annotate('$\Delta = 1.2$', xy=(1, 71), xytext=(1, 76),arrowprops=dict(facecolor='black', arrowstyle='->'))
ax4.annotate('$\Delta = 0.7$', xy=(2, 80), xytext=(1.6, 83),arrowprops=dict(facecolor='black', arrowstyle='->'))
# error
ax4.errorbar(x, hz5000_mic, yerr=[.3, .5, .4], capsize=5)

#y-labels
ax1.set_ylabel('$I$(dB)')
ax3.set_ylabel('$I$(dB)')



plt.show()