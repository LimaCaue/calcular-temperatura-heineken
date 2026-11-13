"""Estima o resfriamento da Heineken pela lei de resfriamento de Newton.

O resultado é uma estimativa: a taxa depende da embalagem e das condições
de resfriamento. O modelo não considera o congelamento da bebida.
"""

from math import exp, isfinite


def calcular_temperatura(inicial, ambiente, minutos, taxa):
    """Retorna a temperatura em °C; a taxa deve ser informada em 1/min."""
    if not all(isfinite(valor) for valor in (inicial, ambiente, minutos, taxa)):
        raise ValueError("Informe apenas números finitos.")
    if minutos < 0 or taxa <= 0:
        raise ValueError("O tempo deve ser zero ou positivo e a taxa, positiva.")
    return ambiente + (inicial - ambiente) * exp(-taxa * minutos)


def ler_numero(mensagem):
    return float(input(mensagem).strip().replace(",", "."))


def main():
    print("Estimativa da temperatura da Heineken")
    print("Este modelo não considera o congelamento da bebida.\n")
    try:
        inicial = ler_numero("Temperatura inicial da cerveja (°C): ")
        ambiente = ler_numero("Temperatura da geladeira ou ambiente (°C): ")
        minutos = ler_numero("Tempo de resfriamento (minutos): ")
        taxa = ler_numero("Taxa de resfriamento (1/min; exemplo hipotético: 0,05): ")
        temperatura = calcular_temperatura(inicial, ambiente, minutos, taxa)
        print(f"\nTemperatura estimada após {minutos:g} min: {temperatura:.1f} °C")
    except ValueError as erro:
        print(f"Dados inválidos: {erro}")


if __name__ == "__main__":
    main()
