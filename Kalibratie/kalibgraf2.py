import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)


hz500_meter = [49.8, 69.8, 79.9]
hz500_mic = [45.1, 64.1, 75.3]
x1=[40, 80]
y1=[40,80]

hz1000_meter = [56.7, 70.7, 79.9]
hz1000_mic = [46.3, 60.6, 69.1]
x2=[45, 80]
y2=[45,80]

hz3000_meter = [58.1,71.3,83.9]
hz3000_mic = [47.5,60.6,72.9]
x3=[45, 80]
y3=[45,80]

hz5000_meter = [49.5,70.5,79.2]
hz5000_mic = [49,69.3,78.5]
x4=[45, 80]
y4=[45,80]


ax1.plot(x1,y1, label='$x=y$')
ax1.legend(loc='upper left')
ax1.errorbar(hz500_meter, hz500_mic, yerr=[2, 1, 1.3], capsize=5)
ax1.set_title('$f$ = $500$ Hz')


ax2.set_title('$f$ = $1000$ Hz')
ax2.plot(x2,y2, label='Referentie')
ax2.errorbar(hz1000_meter, hz1000_mic, yerr=[2.3, 2, 2.7], capsize=5)


ax3.set_title('$f$ = $3000$ Hz')
ax3.plot(x3,y3, label='Referentie')
ax3.errorbar(hz3000_meter, hz3000_mic, yerr=[4.3, 4, 4.7], capsize=5)


ax4.set_title('$f$ = $5000$ Hz')
ax4.plot(x4,y4, label='Referentie')
ax4.errorbar(hz5000_meter, hz5000_mic, yerr=[.3, .5, .4], capsize=5)


ax3.set_xlabel('$I_{meter}$(dB)')
ax4.set_xlabel('$I_{meter}$(dB)')

ax1.set_ylabel('$I_{mic}$(dB)')
ax3.set_ylabel('$I_{mic}$(dB)')

plt.show()