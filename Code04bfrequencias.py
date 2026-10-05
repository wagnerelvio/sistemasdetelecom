import numpy as np
import matplotlib.pyplot as plt

# Frequências em Hz
frequencias = [10, 100, 1000, 10000]
nomes = ["10 Hz", "100 Hz", "1000 Hz", "10000 Hz"]

# Amplitude
A = 1

# Vetor de tempo
# Janela de tempo de 0,1 s
t = np.linspace(0, 0.1, 5000)

# Criar gráfico
plt.figure(figsize=(12, 6))

for f, nome in zip(frequencias, nomes):
    sinal = A * np.sin(2 * np.pi * f * t)
    plt.plot(t, sinal, label=nome)

# Configurações do gráfico
plt.title("Sinais Senoidais Sobrepostos")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
