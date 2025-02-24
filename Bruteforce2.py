import itertools
import multiprocessing
import time

def worker_process(start, end, charset, length, target_password, result_queue):
    charset_len = len(charset)
    for idx in range(start, end):
        attempt = []
        temp = idx
        for _ in range(length):
            attempt.append(charset[temp % charset_len])
            temp //= charset_len
        guess = ''.join(attempt)
        if guess == target_password:
            result_queue.put(guess)  # Send the result to the main process
            return  # Exit once the password is found
    return None

def cpu_brute_force(target_password, max_length, charset):
    start_time = time.time()
    charset_len = len(charset)

    with multiprocessing.Pool() as pool:
        result_queue = multiprocessing.Manager().Queue()  # Shared queue for results

        for length in range(1, max_length + 1):
            total_combinations = int(pow(charset_len, length))
            chunk_size = total_combinations // multiprocessing.cpu_count()

            ranges = [(i * chunk_size, min((i + 1) * chunk_size, total_combinations))
                      for i in range(multiprocessing.cpu_count())]

            # Start workers
            processes = [pool.apply_async(worker_process, (start, end, charset, length, target_password, result_queue))
                         for start, end in ranges]

            # Monitor the result queue
            while True:
                if not result_queue.empty():
                    found_password = result_queue.get()
                    elapsed_time = time.time() - start_time
                    print(f"Password found: {found_password}")
                    print(f"Time taken: {elapsed_time:.2f} seconds")
                    pool.terminate()
                    return
                if all(p.ready() for p in processes):
                    break

    print("Password not found.")

if __name__ == "__main__":
    # Example usage
    target_password = input("Enter the target password to guess: ")
    max_length = int(input("Enter the maximum length of the password: "))
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    print("\nStarting brute force attack...\n")
    cpu_brute_force(target_password, max_length, charset)
