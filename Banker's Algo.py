import numpy as np

def is_safe(processes, available, max_demand, allocation):
    num_processes = len(processes)
    num_resources = len(available)
    
    need = max_demand - allocation
    finish = np.zeros(num_processes, dtype=bool)
    safe_sequence = []
    work = available.copy()
    
    while len(safe_sequence) < num_processes:
        allocated = False
        for i in range(num_processes):
            if not finish[i] and all(need[i] <= work):
                work += allocation[i]
                safe_sequence.append(processes[i])
                finish[i] = True
                allocated = True
                break
        
        if not allocated:
            return False, []
    
    return True, safe_sequence

def main():
    processes = [0, 1, 2, 3, 4]
    available = np.array([3, 3, 2])  # Available resources
    max_demand = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]])  # Max demand of each process
    allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])  # Currently allocated resources
    
    safe, sequence = is_safe(processes, available, max_demand, allocation)
    
    if safe:
        print("System is in a safe state.")
        print("Safe sequence:", sequence)
    else:
        print("System is in an unsafe state. Deadlock may occur.")

if __name__ == "__main__":
    main()
