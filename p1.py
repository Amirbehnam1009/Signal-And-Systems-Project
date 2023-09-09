import numpy as np
import scipy as sp
from scipy.fft import fft, ifft
from scipy import signal
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile
fileToopen = "phase1sample.wav"

(sampFreq, sound) = wavfile.read(fileToopen)  
scale = sp.linspace(0, sampFreq, len(sound))
plot_a = plt.subplot(511)
plot_a.plot(sound[:250])
plot_a.set_title('sound')  





fourierTrans = fft(sound)
plot_b = plt.subplot(512)
plot_b.stem(scale[0:250], np.abs(fourierTrans[0:250]), 'r') 
plot_b.set_title('fourierTrans')


b,a = signal.butter(5, 1000/(sampFreq/2), btype='highpass')  
filteredSignal = signal.lfilter(b,a,sound)  
plot_c = plt.subplot(513)
plot_c.plot(filteredSignal[:250])   
plot_c.set_title('Highpass Filter')  

c,d = signal.butter(5, 1000/(sampFreq/2), btype='lowpass')  
filteredSignal = signal.lfilter(c,d,filteredSignal)  
plot_c = plt.subplot(514)
plot_c.plot(filteredSignal[:250])   
plot_c.set_title('Lowpass Filter')  

wavfile.write("p1.wav", sampFreq, filteredSignal)  

inverseFourierTrans = ifft(filteredSignal)
plot_e = plt.subplot(515)
plot_e.stem(scale[0:250], np.abs(inverseFourierTrans[0:250]), 'r') 
plot_e.set_title('fourierTrans')


plt.show()

