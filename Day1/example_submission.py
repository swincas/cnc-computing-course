import sys
sys.path.append('/home/lhaacke/cnc-computing-course')

if __name__ == "__main__":
    # Allocate approximately 1 GB of memory
    allocated_memory = allocate_memory(1)
    
    # Run for 17 minutes while holding the memory
    hold_memory(17, allocated_memory)

    print("Finished execution.")