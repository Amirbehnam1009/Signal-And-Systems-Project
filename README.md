# 🎵 Signal and Systems Project – Audio Denoising & Equalizer

## 📖 About

> 🎓**Final Project of the Signal and Systems Course**  
> 👨‍🏫Under the supervision of [Prof. Mohammad Rahmati](https://scholar.google.com/citations?user=EYk7M80AAAAJ&hl=en)  
> 🍂Fall 2021 – Amirkabir University of Technology (Tehran Polytechnic)

This repository contains the implementation of a two-phase audio processing project focused on **noise removal** and **frequency band equalization** using Fourier analysis and digital filtering techniques.

---

## 🎯 Phase 1: Audio Denoising

### Objective
Remove noise from an audio signal (`phaseIsample.wav`) using Fourier Transform and frequency-domain filtering.

### Steps Implemented

1. **🔊 Load and Visualize** the audio signal (time domain)
2. **📈 Apply Fourier Transform** to analyze frequency components
3. **🎚️ Identify Noise Frequencies** – weaker amplitudes are considered noise
4. **🧹 Filter Out Noise** by zeroing out non-dominant frequency components
5. **🔄 Apply Inverse Fourier Transform** to reconstruct the denoised signal
6. **📊 Compare and Visualize** original vs. denoised signals

### Key Techniques
- Fast Fourier Transform (FFT)
- Frequency-domain filtering
- Inverse FFT for reconstruction

---

## 🎛️ Phase 2: Simple Equalizer

### Objective
Build a 10-band equalizer that amplifies or attenuates specific frequency bands based on user input.

### Frequency Bands Used
- **Band 1:** 20–50 Hz
- **Band 2:** 50–100 Hz
- **Band 3:** 100–200 Hz
- **Band 4:** 200–500 Hz
- **Band 5:** 500–1000 Hz
- **Band 6:** 1000–2000 Hz
- **Band 7:** 2000–4000 Hz
- **Band 8:** 4000–8000 Hz
- **Band 9:** 8000–12000 Hz
- **Band 10:** 12000–20000 Hz

### Steps Implemented

1. **🎚️ Define Gain Array** – e.g., `[2, 3, 1, 1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1]`
2. **🔧 Apply Gains** to corresponding frequency bands
3. **🔄 Reconstruct Signal** using Inverse FFT
4. **💾 Export** the modified audio file
5. **🎧 Compare** original and equalized audio

### Test Cases
- **Case 1:** Boost frequencies below 1200 Hz, attenuate others
- **Case 2:** Boost frequencies above 2000 Hz, attenuate others

---

## 📦 Repository Structure
``` bash
📂 Signal-And-Systems-Project/
├── 📄 p1.py # Phase 1: Denoising
├── 📄 p2.py # Phase 2: Equalizer
├── 📄 phaseIsample.wav # Sample audio for Phase 1
├── 📄 phase2sample.wav # Sample audio for Phase 2
├── 📄 Final_Project.pdf # Project description (Persian)
├── 📄 README.md # This file
```
## 🛠️ Technologies Used

- **Python** 🐍
- **NumPy**
- **SciPy**
- **Matplotlib**
- **Wave module**

---

## 📊 Sample Results

![Signal Comparison](https://github.com/Amirbehnam1009/Linear-Algebra-Projects/assets/117163007/cef9263c-252b-42ae-b03d-98b56843cacc)

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Amirbehnam1009/Signal-And-Systems-Project.git
   ```
2. Install dependencies:
   ``` bash
   pip install numpy scipy matplotlib
   ```
3. Run each phase:
   ```bash
   python p1.py
   python p2.py
   ```
## 📌 Notes
* This project was completed individually as part of the Signal and Systems course

* The report includes detailed explanations, visualizations, and analysis of each step

* The equalizer allows customizable gain control across 10 frequency bands

## 📬 Contact
For questions or collaborations, feel free to reach out:
https://img.shields.io/badge/GitHub-Amirbehnam1009-blue

## 📜 License
This project is for educational purposes and is part of the academic curriculum at Amirkabir University of Technology.
