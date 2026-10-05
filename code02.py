import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parâmetros do sinal
# -----------------------------
amplitude = 2
frequencia = 10       # Hz
fs = 1000             # frequência de amostragem em Hz
duracao = 1            # segundos

# Vetor de tempo
t = np.arange(0, duracao, 1/fs)

# Sinal senoidal
sinal = amplitude * np.sin(2 * np.pi * frequencia * t)

# -----------------------------
# Gráfico no domínio do tempo
# -----------------------------
plt.figure(figsize=(10, 4))

plt.plot(t, sinal)

plt.title("Sinal no Domínio do Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.xlim(0, 0.5)

plt.show()

# -----------------------------
# FFT para encontrar a frequência
# -----------------------------
fft = np.fft.fft(sinal)

frequencias = np.fft.fftfreq(
    len(sinal),
    1/fs
)

# Considera somente frequências positivas
metade = len(sinal) // 2

frequencias_positivas = frequencias[:metade]

amplitudes_fft = (
    2 / len(sinal)
) * np.abs(fft[:metade])

# -----------------------------
# Gráfico no domínio da frequência
# -----------------------------
plt.figure(figsize=(10, 4))

plt.plot(
    frequencias_positivas,
    amplitudes_fft
)

plt.title("Espectro de Frequência")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")
plt.grid()

plt.xlim(0, 50)

plt.show()

# -----------------------------
# Identificação da frequência
# -----------------------------
indice = np.argmax(amplitudes_fft)

frequencia_detectada = frequencias_positivas[indice]
amplitude_detectada = amplitudes_fft[indice]

print("Amplitude do sinal:", amplitude_detectada)
print("Frequência do sinal:", frequencia_detectada, "Hz")
