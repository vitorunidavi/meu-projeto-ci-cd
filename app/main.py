def soma(a: int, b: int) -> int:
    """Retorna a soma de dois números inteiros."""
    return a + b

def multiplica(a: int, b: int) -> int:
    """Retorna o produto de dois números inteiros."""
    return a * b

if __name__ == "__main__":
    x, y = 5, 3
    print(f"Soma: {soma(x, y)}")
    print(f"Multiplicação: {multiplica(x, y)}")
