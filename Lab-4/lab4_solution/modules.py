def modules(a: int, b: int) -> list[int]:
    """Возвращает список модулей чисел в диапазоне от a до b"""
    if a > b:
        raise ValueError("Число a должно быть меньше числа b")
    return list(abs(i) for i in range(a, b+1))

if __name__ == "__main__":
    print(modules(2, 6))