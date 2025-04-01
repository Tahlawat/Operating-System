class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid  # Process ID
        self.burst_time = burst_time  # Burst time
        self.remaining_time = burst_time  # Remaining execution time
        self.waiting_time = 0  # Waiting time
        self.turnaround_time = 0  # Turnaround time

def round_robin(processes, time_quantum):
    queue = processes.copy()  # Create a queue of processes
    time_elapsed = 0  # Track total time elapsed
    
    while queue:
        process = queue.pop(0)  # Get the first process in the queue
        
        if process.remaining_time > time_quantum:
            time_elapsed += time_quantum  # Increase elapsed time
            process.remaining_time -= time_quantum  # Reduce remaining time
            queue.append(process)  # Reinsert process at the end of the queue
        else:
            time_elapsed += process.remaining_time  # Process finishes execution
            process.waiting_time = time_elapsed - process.burst_time  # Calculate waiting time
            process.turnaround_time = time_elapsed  # Turnaround time is total time taken
    
    return processes

def display_results(processes):
    print("PID\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

# Taking user input
num_processes = int(input("Enter the number of processes: "))
time_quantum = int(input("Enter the time quantum: "))
process_list = []

for i in range(num_processes):
    burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
    process_list.append(Process(i + 1, burst_time))

# Run Round Robin Scheduling
scheduled_processes = round_robin(process_list, time_quantum)

# Display Results
display_results(scheduled_processes)
