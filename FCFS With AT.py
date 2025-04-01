def fcfs_with_arrival(processes):
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time
    n = len(processes)
    
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    completion_time[0] = processes[0][1] + processes[0][2]  # First process completion time
    turnaround_time[0] = completion_time[0] - processes[0][1]
    waiting_time[0] = turnaround_time[0] - processes[0][2]
    
    for i in range(1, n):
        if completion_time[i - 1] < processes[i][1]:  # If CPU is idle before the next process
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = completion_time[i - 1] + processes[i][2]
        
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

# Example Usage
process_list = [(1, 0, 5), (2, 1, 3), (3, 2, 8), (4, 3, 6)]  # (PID, Arrival, Burst)
fcfs_with_arrival(process_list)
