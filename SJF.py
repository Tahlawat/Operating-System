def sjf_scheduling(processes):
    # Sort processes by burst time
    processes.sort(key=lambda x: x[1])  
    
    time = 0
    completion_time = []
    turnaround_time = []
    waiting_time = []
    
    for p in processes:
        arrival, burst = p
        start_time = max(time, arrival)
        finish_time = start_time + burst
        completion_time.append(finish_time)
        turnaround_time.append(finish_time - arrival)
        waiting_time.append(turnaround_time[-1] - burst)
        time = finish_time  # Update current time
    
    # Print results
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i, p in enumerate(processes):
        print(f"P{i+1}\t{p[0]}\t{p[1]}\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

# Example Usage
process_list = [(0, 6), (2, 8), (3, 7), (5, 3)]  # (Arrival Time, Burst Time)
sjf_scheduling(process_list)
