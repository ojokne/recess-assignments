
# part a
class FileHandler:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Example usage:
with FileHandler('example.txt', 'r') as file:
    content = file.read()
    print(content)

# part b
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

# Example usage:
with DatabaseManager('users.db') as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

# part c
import time
from threading import Thread
from multiprocessing import Process

def long_running_task(name, duration):
    print(f"{name} started.")
    time.sleep(duration)
    print(f"{name} finished.")

# Multithreading example
def run_multithreading():
    threads = []
    tasks = [("Task 1", 3), ("Task 2", 5), ("Task 3", 2)]

    for task in tasks:
        thread = Thread(target=long_running_task, args=task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Multiprocessing example
def run_multiprocessing():
    processes = []
    tasks = [("Task 1", 3), ("Task 2", 5), ("Task 3", 2)]

    for task in tasks:
        process = Process(target=long_running_task, args=task)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Run multithreading example
print("Running multithreading example:")
run_multithreading()

# Run multiprocessing example
print("\nRunning multiprocessing example:")
run_multiprocessing()
