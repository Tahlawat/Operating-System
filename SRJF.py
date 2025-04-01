import heapq

def sjf_preemptive(processes):
    processes.sort()  # Sort by arrival time
    n = len(processes)
    
    time = 0
    completed = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = [bt for _, bt in processes]
    min_heap = []  # (burst_time, index)
    process_index = 0
    
    while completed < n:
        # Add available processes to the heap
        while process_index < n and processes[process_index][0] <= time:
            heapq.heappush(min_heap, (remaining_time[process_index], process_index))
            process_index += 1
        
        if min_heap:
            # Select process with shortest remaining time
            burst, index = heapq.heappop(min_heap)
            time += 1  # Execute for 1 time unit
            remaining_time[index] -= 1
            
            # If process completes
            if remaining_time[index] == 0:
                completed += 1
                completion_time = time
                turnaround_time[index] = completion_time - processes[index][0]
                waiting_time[index] = turnaround_time[index] - processes[index][1]
            else:
                # Push back with updated burst time
                heapq.heappush(min_heap, (remaining_time[index], index))
        else:
            time += 1  # CPU idle
        
    # Print results
    print("Process\tArrival\tBurst\tTurnaround\tWaiting")
    for i, p in enumerate(processes):
        print(f"P{i+1}\t{p[0]}\t{p[1]}\t{turnaround_time[i]}\t\t{waiting_time[i]}")

# Example Usage
process_list = [(0, 6), (2, 8), (3, 7), (5, 3)]  # (Arrival Time, Burst Time)
sjf_preemptive(process_list)
