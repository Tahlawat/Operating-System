import threading
import time

# Initialize semaphores and shared resources
read_count = 0
mutex = threading.Semaphore(1)  # For read_count synchronization
write_lock = threading.Semaphore(1)  # To ensure only one writer at a time

def reader(reader_id):
    global read_count
    while True:
        time.sleep(1)  # Simulating random reading interval
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            write_lock.acquire()  # First reader locks writers
        mutex.release()
        
        # Reading section
        print(f"Reader {reader_id} is reading.")
        time.sleep(2)  # Simulate reading time
        
        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            write_lock.release()  # Last reader unlocks writers
        mutex.release()

def writer(writer_id):
    while True:
        time.sleep(3)  # Simulating random writing interval
        write_lock.acquire()
        
        # Writing section
        print(f"Writer {writer_id} is writing.")
        time.sleep(2)  # Simulate writing time
        
        write_lock.release()

# Creating multiple reader and writer threads
num_readers = 3
num_writers = 2

threads = []
for i in range(num_readers):
    t = threading.Thread(target=reader, args=(i + 1,))
    threads.append(t)
    t.start()

for i in range(num_writers):
    t = threading.Thread(target=writer, args=(i + 1,))
    threads.append(t)
    t.start()

# Join threads (optional, as they run infinitely)
for t in threads:
    t.join()
