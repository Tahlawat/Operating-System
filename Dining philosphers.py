import threading
import time

# Number of philosophers
num_philosophers = 5

# Semaphore for each fork
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

# A semaphore to prevent deadlock by allowing only (N-1) philosophers to pick up forks at the same time
max_diners = threading.Semaphore(num_philosophers - 1)

def philosopher(philosopher_id):
    while True:
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(1)
        
        max_diners.acquire()  # Limit the number of philosophers eating at the same time
        
        # Pick up left and right forks
        left_fork = forks[philosopher_id]
        right_fork = forks[(philosopher_id + 1) % num_philosophers]
        
        left_fork.acquire()
        right_fork.acquire()
        
        # Eating
        print(f"Philosopher {philosopher_id} is eating.")
        time.sleep(2)
        
        # Put down forks
        left_fork.release()
        right_fork.release()
        
        max_diners.release()  # Allow another philosopher to eat

# Create philosopher threads
threads = []
for i in range(num_philosophers):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

# Join threads (optional, since they run indefinitely)
for t in threads:
    t.join()
