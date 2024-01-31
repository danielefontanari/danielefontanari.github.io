import multiprocessing
import time

def increment_and_write(process_id, modulo, filename_prefix):
    filename = f"{filename_prefix}_{process_id}.txt"
    number = process_id  # Starting number for this process
    while True:
        with open(filename, "a") as f:
            f.write(f"{number}\n")
        number += modulo  # Increment by the number of processes
        time.sleep(1)  # Wait for a second

if __name__ == "__main__":
    num_processes = 4  # Number of parallel processes
    filename_prefix = "output"

    # Create and start a separate process for each class of equivalence
    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=increment_and_write, args=(i, num_processes, filename_prefix))
        processes.append(p)
        p.start()

    # Wait for all processes to finish (they won't in this infinite loop example)
    for p in processes:
        p.join()