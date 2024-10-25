import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

def generate_password(length: int = 12) -> str:
    """Возвращает строку с паролем из случайно выбранных символов строки chars"""
    if length <=0:
        raise ValueError("Длина не может быть меньше либо равна 0")
    return ''.join(random.choice(chars) for _ in range(length))

def generate_passwords(password_length: int = 12, passwords_count: int = 5) -> list[str]:
    """Возвращает список случайно сгенерированных паролей функции generate_password()"""
    if passwords_count <= 0:
        raise ValueError("Количество генерируемых паролей не может быть меньше либо равно 0")

    return list(generate_password(password_length) for _ in range(passwords_count))

if __name__ == "__main__":
    print(generate_passwords())