import random
from string import ascii_lowercase, ascii_uppercase
import threading

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

def generate_password(length: int = 12) -> str:
    """Возвращает строку с паролем из случайно выбранных символов строки chars"""
    if length <= 0:
        raise ValueError("Длина не может быть меньше либо равна 0")
    return ''.join(random.choice(chars) for _ in range(length))

def worker(password_length: int, passwords_count: int, result_list):
    passwords = [generate_password(password_length) for _ in range(passwords_count)]
    result_list.extend(passwords)

def generate_passwords_multithreaded(password_length: int = 12, passwords_count: int = 5, threads_count: int = 5) -> list[str]:
    """Возвращает список случайно сгенерированных паролей в многопоточном режиме"""
    if passwords_count <= 0:
        raise ValueError("Количество генерируемых паролей не может быть меньше либо равно 0")

    result_list = []
    threads = []

    passwords_per_thread = passwords_count // threads_count
    remaining_passwords = passwords_count % threads_count

    for i in range(threads_count):
        thread_passwords_count = passwords_per_thread + (1 if i < remaining_passwords else 0)
        thread = threading.Thread(target=worker, args=(password_length, thread_passwords_count, result_list))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return result_list

if __name__ == "__main__":
    print(generate_passwords_multithreaded())