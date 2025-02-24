CPU Brute Force Password Cracker
This project implements a CPU-based brute force password cracker in Python using multiprocessing. The script attempts to guess a target password by iterating through all possible combinations of characters up to a specified length.

Features
Multiprocessing: Uses Python's multiprocessing module to distribute the workload across available CPU cores.
Customizable Charset: Supports a customizable set of characters (e.g., alphanumeric).
Dynamic Length: Allows you to specify the maximum length of the password to attempt.
Real-time Result: Outputs the password and time taken once a match is found.
How It Works
Worker Process: Each worker process is assigned a range of possible password combinations to check.
Combination Generation: For each password length, the script generates all possible combinations based on the provided character set.
Multiprocessing Pool: The work is distributed among available CPU cores to accelerate the search.
Result Queue: Once a worker finds the target password, it communicates the result back to the main process, which terminates the pool and outputs the result.
