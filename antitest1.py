import numpy as np
import matplotlib.pyplot as plt


Fs = 1000             
T = 1.0/Fs         
t = np.linspace(0.0,1.0,int(Fs))
f1 = 150   
f2 = 120  
segnale = np.sin(2.0*np.pi*f1*t)+0.5*np.sin(2.0*np.pi*f2*t)
N = len(t)
fft_result = np.fft.fft(segnale)
segnale_ricostruito = np.fft.ifft(fft_result)
plt.figure(figsize=(10, 5))
plt.plot(t, segnale, label='Segnale originale')
plt.plot(t, segnale_ricostruito.real, '--', label='Segnale ricostruito')
plt.legend()
plt.xlabel('Tempo [s]')
plt.ylabel('Ampiezza')
plt.title('Trasformata e Antitrasformata di Fourier')
plt.grid(True)
plt.show()