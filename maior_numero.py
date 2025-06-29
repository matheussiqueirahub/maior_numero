def maior_numero(a: float, b: float, c: float) -> float:
    """
    Retorna o maior entre três números.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    try:
        nums = [
            float(input("Digite o primeiro número: ")),
            float(input("Digite o segundo número: ")),
            float(input("Digite o terceiro número: "))
        ]
    except ValueError:
        print("Erro: insira apenas números válidos.")
    else:
        print(f"O maior número é: {maior_numero(*nums)}")
