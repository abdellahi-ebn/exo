def minimum_energy_to_reach_intersections(n, shortcuts):
    energy = [float('inf')] * n
    energy[0] = 0  
    queue = [0] 
    head = 0  
    
    while head < len(queue):
        current = queue[head]
        head += 1
        
        if current + 1 < n and energy[current + 1] > energy[current] + 1:
            energy[current + 1] = energy[current] + 1
            queue.append(current + 1)
        
        if current - 1 >= 0 and energy[current - 1] > energy[current] + 1:
            energy[current - 1] = energy[current] + 1
            queue.append(current - 1)
        
        shortcut_destination = shortcuts[current] - 1  
        if shortcut_destination < n and energy[shortcut_destination] > energy[current] + 1:
            energy[shortcut_destination] = energy[current] + 1
            queue.append(shortcut_destination)
    
    return energy

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    shortcuts = list(map(int, data[1:n+1]))
    
    minimum_energies = minimum_energy_to_reach_intersections(n, shortcuts)
    print(' '.join(map(str, minimum_energies)))

if __name__ == "__main__":
    main()

