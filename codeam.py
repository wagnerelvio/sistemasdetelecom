import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Parâmetros
# ---------------------------------

Am = 1          # amplitude do sinal de informação
fm = 100        # frequência do sinal modulante = 100 Hz

Ac = 1          # amplitude da portadora
fc = 2000       # frequência da portadora = 2 kHz

mu = 0.8        # índice de modulação = 80%

fs = 100000     # frequência de amostragem
duracao = 0.03  # 30 ms

# Vetor de tempo
t = np.arange(0, duracao, 1/fs)

# ---------------------------------
# Sinal de informação
# ---------------------------------

m = Am * np.cos(2 * np.pi * fm * t)

# ---------------------------------
# Portadora
# ---------------------------------

c = Ac * np.cos(2 * np.pi * fc * t)

# ---------------------------------
# Sinal AM
# ---------------------------------

s_am = Ac * (1 + mu * m) * np.cos(2 * np.pi * fc * t)

# ---------------------------------
# Gráficos
# ---------------------------------

plt.figure(figsize=(12, 8))

# Sinal de informação
plt.subplot(3, 1, 1)

plt.plot(t, m)

plt.title("Sinal de Informação ou Modulante - 100 Hz")
plt.ylabel("Amplitude")
plt.grid()

# Portadora
plt.subplot(3, 1, 2)

plt.plot(t, c)

plt.title("Portadora - 2 kHz")
plt.ylabel("Amplitude")
plt.grid()

# Sinal AM
plt.subplot(3, 1, 3)

plt.plot(t, s_am)

# Envoltória
plt.plot(t, Ac * (1 + mu * m), "--")
plt.plot(t, -Ac * (1 + mu * m), "--")

plt.title("Sinal Modulado em Amplitude - AM")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
