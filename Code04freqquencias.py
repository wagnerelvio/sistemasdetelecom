import numpy as np
import matplotlib.pyplot as plt

# Frequências que serão analisadas
frequencias = [
    10,          # 10 Hz
    100,         # 100 Hz
    1_000,       # 1 kHz
    10_000,      # 10 kHz
    10_000_000,  # 10 MHz
    100_000_000  # 100 MHz
]

nomes = [
    "10 Hz",
    "100 Hz",
    "1 kHz",
    "10 kHz",
    "10 MHz",
    "100 MHz"
]

# Amplitude dos sinais
A = 1

# Número de períodos que serão mostrados
numero_periodos = 3

for f, nome in zip(frequencias, nomes):

    # Período do sinal
    T = 1 / f

    # Tempo equivalente a 3 períodos
    duracao = numero_periodos * T

    # 100 pontos por período
    t = np.linspace(
        0,
        duracao,
        numero_periodos * 1000
    )

    # Sinal senoidal
    sinal = A * np.sin(2 * np.pi * f * t)

    # Gráfico
    plt.figure(figsize=(10, 4))

    plt.plot(t, sinal)

    plt.title(
        f"Sinal Senoidal - Frequência = {nome}"
    )

    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")

    plt.grid()

    plt.ylim(-1.2, 1.2)

    plt.show()

    # Mostrar informações
    print("--------------------------------")
    print("Frequência:", nome)
    print("Frequência em Hz:", f)
    print("Período:", T, "s")
