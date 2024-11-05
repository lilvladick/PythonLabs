import threading

def multiply_arrays_pairs(list1, list2):
    """Возвращает generator expression с перемноженными парами чисел из массивов"""
    return (x*y for x, y in zip(list1, list2))

def worker(lock, generator):
    with lock:
        try:
            value = next(generator)
            print(f"Thread got: {value}")
        except StopIteration:
            print("Generator is exhausted")

if __name__ == "__main__":
    generator = multiply_arrays_pairs([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    lock = threading.Lock()

    threads = []
    for _ in range(3):
        thread = threading.Thread(target=worker, args=(lock, generator))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()