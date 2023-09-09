import numpy as np
import scipy as sp
from scipy.fft import fft, ifft
from scipy import signal
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile





def create_filter(data, l, h, sampFreq):
    low = l / sampFreq
    high = h / sampFreq
    b, a = signal.butter(5, [low, high], btype='bandpass')
    filtered = signal.lfilter(b, a, data)
    return filtered

def equalizer (data, fs, l):

    band1 = create_filter(data, 20, 50, fs)*l[0]
    band2 = create_filter(data, 50, 100, fs)*l[1]
    band3 = create_filter(data, 100, 200, fs)*l[2]
    band4 = create_filter(data, 200, 500, fs)*l[3]
    band5 = create_filter(data, 500, 1000, fs)*l[4]
    band6 = create_filter(data, 1000, 2000, fs)*l[5]
    band7 = create_filter(data, 2000, 4000, fs)*l[6]
    band8 = create_filter(data, 4000, 8000, fs)*l[7]
    band9 = create_filter(data, 8000, 12000, fs)*l[8]
    band10 = create_filter(data, 12000, 20000, fs)* l[9]
    signal = band1 + band2 + band3 + band4 + band5 + band6 + band7 + band8 + band9 + band10
    return signal

fileToopen = "phase2sample.wav"

(sampFreq, sound) = wavfile.read(fileToopen)  
scale = sp.linspace(0, sampFreq, len(sound))

fourierTrans = fft(sound)



b,a = signal.butter(5, 1000/(sampFreq/2), btype='highpass')  
filteredSignal = signal.lfilter(b,a,sound)  


c,d = signal.butter(5, 1000/(sampFreq/2), btype='lowpass')  
filteredSignal = signal.lfilter(c,d,filteredSignal)  

signal = equalizer(filteredSignal,sampFreq, [2,3,1,1,0.2,0.2,0.1,0.1,0.1,0.1])

wavfile.write("p2.wav", sampFreq, filteredSignal)  

inverseFourierTrans = ifft(filteredSignal)

