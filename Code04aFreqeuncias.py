import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Definição das frequências
# -----------------------------
freqs_baixas = [10, 100, 1_000, 10_000]          # Hz
labels_baixas = ["10 Hz", "100 Hz", "1 kHz", "10 kHz"]

freqs_altas = [10_000_000, 100_000_000]          # Hz
labels_altas = ["10 MHz", "100 MHz"]

A = 1  # amplitude

# -----------------------------
# 1) Gráfico sobreposto - baixas frequências
# -----------------------------
# Janela de tempo para visualizar bem 10 Hz até 10 kHz
t1 = np.linspace(0, 0.3, 5000)   # 0,3 s

plt.figure(figsize=(12, 5))

for f, label in zip(freqs_baixas, labels_baixas):
    sinal = A * np.sin(2 * np.pi * f * t1)
    plt.plot(t1, sinal, label=label)

plt.title("Sinais Sobrepostos - 10 Hz, 100 Hz, 1 kHz e 10 kHz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# -----------------------------
# 2) Gráfico sobreposto - altas frequências
# -----------------------------
# Janela muito pequena para visualizar MHz
t2 = np.linspace(0, 0.3e-6, 5000)   # 0,3 microssegundos

plt.figure(figsize=(12, 5))

for f, label in zip(freqs_altas, labels_altas):
    sinal = A * np.sin(2 * np.pi * f * t2)
    plt.plot(t2, sinal, label=label)

plt.title("Sinais Sobrepostos - 10 MHz e 100 MHz")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
