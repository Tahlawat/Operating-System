def fcfs_without_arrival(processes):
    n = len(processes)
    
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    completion_time[0] = processes[0][1]  # First process completion time
    turnaround_time[0] = completion_time[0]
    waiting_time[0] = 0
    
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + processes[i][1]
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - processes[i][1]

    print("\nProcess\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

# Example Usage
process_list = [(1, 5), (2, 3), (3, 8), (4, 6)]  # (PID, Burst)
fcfs_without_arrival(process_list)
