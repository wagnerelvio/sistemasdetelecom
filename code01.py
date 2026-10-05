import numpy as np
import matplotlib.pyplot as plt

# Frequencia de amostragem
fs = 500_000

# Duracao da simulacao
duracao = 0.005

# Vetor de tempo
t = np.arange(0, duracao, 1/fs)

# Frequencia do audio
fm = 1000

# Frequencia da portadora
fc = 20000

# Amplitudes
Am = 1
Ac = 1

# Indice de modulacao AM
mu = 0.8

# Indice de modulacao FM
beta = 5

# Sinal de audio
audio = Am * np.sin(2 * np.pi * fm * t)

# Portadora
portadora = Ac * np.cos(2 * np.pi * fc * t)

# Modulacao AM
sinal_am = Ac * (1 + mu * audio) * \
           np.cos(2 * np.pi * fc * t)

# Modulacao FM
sinal_fm = Ac * np.cos(
    2 * np.pi * fc * t
    + beta * np.sin(2 * np.pi * fm * t)
)

# Graficos
plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(t * 1000, audio)
plt.title("1 - Sinal de Audio")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t * 1000, portadora)
plt.title("2 - Sinal da Portadora")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t * 1000, sinal_am)
plt.title("3 - Modulacao AM")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t * 1000, sinal_fm)
plt.title("4 - Modulacao FM")
plt.ylabel("Amplitude")
plt.xlabel("Tempo (ms)")
plt.grid(True)

plt.tight_layout()
plt.show()
