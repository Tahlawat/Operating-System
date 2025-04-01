def fifo_page_replacement(pages, capacity):
    memory, page_faults = [], 0
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
    return page_faults

def lru_page_replacement(pages, capacity):
    memory, page_faults, recent = [], 0, {}
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: recent.get(p, -1))
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        recent[page] = i
    return page_faults

def optimal_page_replacement(pages, capacity):
    memory, page_faults = [], 0
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                future_uses = {p: (pages[i+1:].index(p) if p in pages[i+1:] else float('inf')) for p in memory}
                to_replace = max(future_uses, key=future_uses.get)
                memory.remove(to_replace)
                memory.append(page)
            page_faults += 1
    return page_faults

# User input
pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
capacity = int(input("Enter the number of frames: "))

# Running algorithms
fifo_faults = fifo_page_replacement(pages, capacity)
lru_faults = lru_page_replacement(pages, capacity)
optimal_faults = optimal_page_replacement(pages, capacity)

# Display results
print(f"FIFO Page Faults: {fifo_faults}")
print(f"LRU Page Faults: {lru_faults}")
print(f"Optimal Page Faults: {optimal_faults}")
