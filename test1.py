import numpy as np
import matplotlib.pyplot as plt


Fs = 1000             
T = 1.0/Fs         
t = np.linspace(0.0,1.0,int(Fs))
f1 = 150   
f2 = 120  
signal = np.sin(2.0*np.pi*f1*t)+0.5*np.sin(2.0*np.pi*f2*t)
N = len(t)
fft_result = np.fft.fft(signal)
frequenze = np.fft.fftfreq(N, T)
plt.figure(figsize=(10, 4))
plt.plot(frequenze[:N//2],2.0/N*np.abs(fft_result[:N//2]))
plt.title("Trasformata di Fourier (FFT)")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Ampiezza")
plt.grid(True)
plt.tight_layout()
plt.show()
