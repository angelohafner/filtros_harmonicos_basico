# -*- coding: utf-8 -*-
"""Filtro Amortecido.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JTrSN7PnJ7OO4Y-fvOH9BMUEOgNcs4pL
"""

import numpy as np


def frequencia_sintonia(L_mH, C_uF):
    """
    Calcula a frequência de sintonia de um filtro LC.

    Parâmetros:
    L (float): Indutância em henries (H).
    C (float): Capacitância em farads (F).

    Retorna:
    float: Frequência de sintonia em hertz (Hz).
    """
    L = L_mH * 1e-3  # Convertendo para H
    C = C_uF * 1e-6  # Convertendo para F
    if L <= 0 or C <= 0:
        raise ValueError("A indutância (L) e a capacitância (C) devem ser maiores que zero.")

    f = 1 / (2 * np.pi * np.sqrt(L * C))
    return f

# Funções de cálculo
def calcular_impedancia_amortecido(R, r, L, C,w):
    """
    Calcula a impedância de cada elemento (R, L e C).
    """
    Z_R = complex(R, 0)                     # Impedância do resistor
    Z_L = complex(r, w * L * 1e-3)          # Impedância do indutor (L em mH)
    Z_C = complex(0, -1 / (w * C * 1e-6))   # Impedância do capacitor (C em uF)
    Z_RL = 1 / ( 1/Z_R + 1/Z_L )            # Impedância em paralela entre R e L
    Z_F = Z_RL + Z_C                    # Impedância total
    return Z_R, Z_L, Z_C, Z_RL, Z_F

def calcular_corrente_tensao(V_linha, Z_R, Z_L, Z_C, Z_RL, Z_F):
    """
    Calcula a corrente em cada elemento a partir da tensão de linha.
    """
    V_fase = V_linha / np.sqrt(3)

    I_F = V_fase / Z_F

    V_R = I_F * Z_RL
    V_L = I_F * Z_RL
    V_C = I_F * Z_C
    V_F = V_R + V_C

    I_R = V_R / Z_R
    I_L = V_L / Z_L
    I_C = V_C / Z_C


    return I_R, I_L, I_C, I_F, V_R, V_L, V_C, V_F


def calcular_potencia(I_R, I_L, I_C, I_F, V_R, V_L, V_C, V_F):
    """
    Calcula a potência em cada elemento. Considera a tensão de fase e a corrente em cada componente.
    """
    P_R = V_R * np.conj(I_R)
    P_L = V_L * np.conj(I_L)
    P_C = V_C * np.conj(I_C)
    P_F = V_F * np.conj(I_F)

    return P_R, P_L, P_C, P_F

# Função principal para cálculo dos parâmetros do filtro
def calcular_filtro_estrela(R, r, L, C, V_linha, w):
    """
    Função principal para calcular impedâncias, correntes, tensões e potências no filtro em estrela.
    """
    # Cálculo das impedâncias
    Z_R, Z_L, Z_C, Z_RL, Z_F = calcular_impedancia_amortecido(R, r, L, C, w)

    # Cálculo da corrente em cada elemento
    I_R, I_L, I_C, I_F, V_R, V_L, V_C, V_F = calcular_corrente_tensao(V_linha, Z_R, Z_L, Z_C, Z_RL, Z_F)

    # Cálculo da potência em cada elemento
    P_R, P_L, P_C, P_F = calcular_potencia(I_R, I_L, I_C, I_F, V_R, V_L, V_C, V_F)

    # Resultado formatado como dicionário
    resultados_formatados = {
        "Impedancia": {
            "R": (f"{np.abs(Z_R):.2f} ∠ {np.angle(Z_R, deg=True):.2f}°"),
            "L": (f"{np.abs(Z_L):.2f} ∠ {np.angle(Z_L, deg=True):.2f}°"),
            "C": (f"{np.abs(Z_C):.2f} ∠ {np.angle(Z_C, deg=True):.2f}°"),
            "Filtro": (f"{np.abs(Z_F):.2f} ∠ {np.angle(Z_F, deg=True):.2f}°")
        },
        "Corrente": {
            "R": (f"{np.abs(I_R):.2f} ∠ {np.angle(I_R, deg=True):.2f}°"),
            "L": (f"{np.abs(I_L):.2f} ∠ {np.angle(I_L, deg=True):.2f}°"),
            "C": (f"{np.abs(I_C):.2f} ∠ {np.angle(I_C, deg=True):.2f}°"),
            "Filtro": (f"{np.abs(I_F):.2f} ∠ {np.angle(I_F, deg=True):.2f}°")
        },
        "Tensao": {
            "R": (f"{np.abs(V_R):.2f} ∠ {np.angle(V_R, deg=True):.2f}°"),
            "L": (f"{np.abs(V_L):.2f} ∠ {np.angle(V_L, deg=True):.2f}°"),
            "C": (f"{np.abs(V_C):.2f} ∠ {np.angle(V_C, deg=True):.2f}°"),
            "Filtro": (f"{np.abs(V_F):.2f} ∠ {np.angle(V_F, deg=True):.2f}°")
        },
        "Potencia": {
            "R": f"{3 * np.real(P_R) / 1e6:.2f} MW",
            "L": f"{3 * np.imag(P_L) / 1e6:.2f} MVAr",
            "C": f"{3 * np.imag(P_C) / 1e6:.2f} MVAr",
            "Filtro": f"{3 * P_F / 1e6:.2f} MVA"
        }
    }

    # Retornando o dicionário e os valores individuais
    return (
        resultados_formatados,
        Z_R, Z_L, Z_C, Z_F,
        I_R, I_L, I_C, I_F,
        V_R, V_L, V_C, V_F,
        P_R, P_L, P_C, P_F
    )

def celulas(nr_cap_serie, nr_cap_paral, V_C, P_C, sobretensao_capacitores):
    qt_cap = 3 * nr_cap_serie * nr_cap_paral
    tensao_nominal_celula = np.abs(V_C) * sobretensao_capacitores / nr_cap_serie
    potencia_nominal_celula = 3 * np.abs(P_C) * sobretensao_capacitores**2 / qt_cap
    capacitancia_nominal_celula = 1 / ( w1 * tensao_nominal_celula **2 / potencia_nominal_celula )
    capacitancia_associacao = capacitancia_nominal_celula * nr_cap_paral / nr_cap_serie

    return qt_cap, tensao_nominal_celula, potencia_nominal_celula, capacitancia_nominal_celula, capacitancia_associacao


# Exibir o dicionário resultado_formatado de forma organizada
def exibir_resultados(resultados):
    for categoria, valores in resultados.items():
        print(f"=== {categoria} ===")
        for elemento, valor in valores.items():
            print(f"{elemento}: {valor}")
        print("\n")

#############################################################################################
# Os dados de entrada iniciam aqui
f1 = 60
w1 = 2 * np.pi * f1
R = 222      # Resistencia em ohms
r = 0.792        # resistência do indutor -->0
L = 34.303     # Indutancia em mH
C = 8.543       # Capacitancia em uF
V_linha = 34.5  # Tensao de linha em kV
sobretensao_capacitores = 1.3
nr_cap_serie = 2
nr_cap_paral = 2
# Os dados de entrada terminam aqui
#############################################################################################


resultado_formatado, Z_R, Z_L, Z_C, Z_F, I_R, I_L, I_C, I_F, V_R, V_L, V_C, V_F, P_R, P_L, P_C, P_F = calcular_filtro_estrela(R, r, L, C, V_linha * 1e3, w1)
qt_cap, tensao_nominal_celula, potencia_nominal_celula, capacitancia_nominal_celula, capacitancia_associacao = celulas(nr_cap_serie, nr_cap_paral, V_C, P_C, sobretensao_capacitores)

print("================ Filtro ===============")
print(f"Potencia do Filtro: {3*P_F/1e6:.2} MVA ")
print(f"Capacitância do Filtro: {C:.4} uF ")
print(f"Tensão de trabalho do capacitor: {np.abs(V_C)/1000:.4} kV  [{np.abs(V_C)/np.abs(V_F):.3}]")
print(f"Tensão considerada com sobretensão do capacitor: {sobretensao_capacitores*np.abs(V_C)/1000:.4} kV ")
print(f"Frquencia de sintonia: {frequencia_sintonia(L, C):.4} Hz")
print("=======================================")
print("")
print("========= Células Capacitivas =========")
print(f"Quantidade de células:  {qt_cap:.0f}, série={nr_cap_serie:.0f}, paralelo={nr_cap_paral}")
print(f"Tensão da célula:        {tensao_nominal_celula/1e3:.4} kV ")
print(f"Potência da célula:      {potencia_nominal_celula/1e3:.4} kVAr ")
print(f"Capacitância da célula:  {capacitancia_nominal_celula*1e6:.4} uF ")
print("=======================================")
print("")
print("================ Banco ===============")
print(f"Tensão do banco:         {np.sqrt(3)*sobretensao_capacitores*np.abs(V_C)/1000:.4} kV ")
print(f"Potência do banco:       {qt_cap*potencia_nominal_celula/1e6:.4} MVAr ")
print(f"Capacitância do banco:   {capacitancia_nominal_celula*nr_cap_paral/nr_cap_serie*1e6:.4} uF ")
print("=======================================")

exibir_resultados(resultado_formatado)