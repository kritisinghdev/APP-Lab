"""Experiment 13: Create multiple threads to perform different tasks
concurrently  -- CO-5"""

import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(f"[Numbers] {i}")
        time.sleep(0.5)


def print_letters():
    for ch in "ABCDE":
        print(f"[Letters] {ch}")
        time.sleep(0.5)


def calculate_squares():
    for i in range(1, 6):
        print(f"[Squares] {i} squared = {i * i}")
        time.sleep(0.5)


# A shared counter protected by a Lock (prevents race conditions)
counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1


if __name__ == "__main__":
    # Part 1: three different tasks running at the same time
    threads = [
        threading.Thread(target=print_numbers),
        threading.Thread(target=print_letters),
        threading.Thread(target=calculate_squares),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()                      # wait for all threads to finish
    print("All tasks finished.\n")

    # Part 2: threads sharing data safely
    workers = [threading.Thread(target=increment) for _ in range(4)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    print("Counter value (expected 40000):", counter)
