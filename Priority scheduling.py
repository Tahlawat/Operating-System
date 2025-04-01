class Process:
    # Process class to store process ID, burst time, priority, and calculated times
    def __init__(self, pid, burst_time, priority):
        self.pid = pid  # Process ID
        self.burst_time = burst_time  # Burst time (execution time required)
        self.priority = priority  # Priority of the process (lower value = higher priority)
        self.waiting_time = 0  # Time process has to wait before execution
        self.turnaround_time = 0  # Time from arrival to completion

def priority_scheduling(processes):
    # Sort processes based on priority (higher priority first, assuming lower number is higher priority)
    processes.sort(key=lambda x: x.priority)  # Sorting based on priority value
    
    # Initialize total waiting and turnaround times for averaging later
    total_waiting_time = 0
    total_turnaround_time = 0
    
    # First process has no waiting time
    processes[0].waiting_time = 0  
    processes[0].turnaround_time = processes[0].burst_time  # Turnaround time = burst time for the first process
    
    # Calculate waiting time and turnaround time for all other processes
    for i in range(1, len(processes)):
        # Waiting time = previous process's waiting time + previous process's burst time
        processes[i].waiting_time = processes[i - 1].waiting_time + processes[i - 1].burst_time
        
        # Turnaround time = waiting time + burst time of the process
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time
        
        # Accumulate total waiting and turnaround times for averaging
        total_waiting_time += processes[i].waiting_time
        total_turnaround_time += processes[i].turnaround_time
    
    # Calculate average waiting time and turnaround time
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    
    return processes, avg_waiting_time, avg_turnaround_time

def display_results(processes, avg_waiting_time, avg_turnaround_time):
    # Display the table header
    print("PID\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    
    # Print details of each process
    for process in processes:
        print(f"{process.pid}\t{process.priority}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
    
    # Display average waiting time and turnaround time
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# Example usage with predefined process list
process_list = [
    Process(1, 10, 2),  # Process 1 with burst time 10 and priority 2
    Process(2, 5, 1),   # Process 2 with burst time 5 and priority 1 (highest priority)
    Process(3, 8, 3)    # Process 3 with burst time 8 and priority 3
]

# Call the scheduling function
scheduled_processes, avg_wt, avg_tt = priority_scheduling(process_list)

# Display the results
display_results(scheduled_processes, avg_wt, avg_tt)
