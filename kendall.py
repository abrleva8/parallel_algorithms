import random
import time

import matplotlib.pyplot as plt
from multiprocessing import Pool, freeze_support

def create_data(data_size: int) -> tuple[list[float], list[float]]:
    """Generate two lists of random floating-point numbers.

        Args:
            data_size: The number of random numbers to generate in each list.

        Returns:
            Tuple containing two lists: x and y, each with random float values.
    """
    x = [random.uniform(0, 100) for _ in range(data_size)]  # Generate random numbers for x
    y = [random.uniform(0, 100) for _ in range(data_size)]  # Generate random numbers for y
    return x, y

def timing_decorator(func):
    """Decorator to measure execution time of a function and return it."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time  # Return both the result and execution time
    return wrapper

def count_concordant_discordant(i: int, x: list[float], y: list[float]) -> tuple[int, int]:
    """Count concordant and discordant pairs for a specific index i."""
    concordant = 0
    discordant = 0
    n = len(x)

    for j in range(i + 1, n):
        if (x[i] - x[j]) * (y[i] - y[j]) > 0:
            concordant += 1
        elif (x[i] - x[j]) * (y[i] - y[j]) < 0:
            discordant += 1

    return concordant, discordant

@timing_decorator
def kendall_tau_multi_thread(x: list[float], y: list[float], num_processes: int) -> tuple[float, int, int]:
    """Calculate Kendall's Tau using a multiprocessing approach."""
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")

    n = len(x)
    total_concordant = 0
    total_discordant = 0

    # Use Pool to calculate concordant and discordant pairs in parallel
    with Pool(processes=num_processes) as pool:
        results = pool.starmap(count_concordant_discordant, [(i, x, y) for i in range(n)])

    # Aggregate results
    for concordant, discordant in results:
        total_concordant += concordant
        total_discordant += discordant

    # Calculate Kendall's Tau
    tau = (total_concordant - total_discordant) / ((n * (n - 1)) / 2)

    return tau, total_concordant, total_discordant

@timing_decorator
def kendall_tau_single_thread(x: list[float], y: list[float])-> tuple[float, int, int]:
    """Calculate Kendall's Tau using a single-threaded approach."""
    n = len(x)
    total_concordant = 0
    total_discordant = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (x[i] - x[j]) * (y[i] - y[j]) > 0:
                total_concordant += 1
            elif (x[i] - x[j]) * (y[i] - y[j]) < 0:
                total_discordant += 1

    # Calculate Kendall's Tau
    tau = (total_concordant - total_discordant) / ((n * (n - 1)) / 2)

    return tau, total_concordant, total_discordant

def calculates_times(size: int) -> list[float]:
    """Calculate execution times for Kendall's Tau with different numbers of processes.

        Args:
            size: The number of data points to generate for the calculations.

        Returns:
            List of execution times, where the first element is the time for single-threaded
            and the subsequent elements are for multi-threaded with increasing processes.
    """

    x, y = create_data(size)
    tau_single, execution_time_single = kendall_tau_single_thread(x, y)
    times = [0, execution_time_single]
    for num_processes in range(2, 9):
        tau_parallel, execution_time_parallel = kendall_tau_multi_thread(x, y, num_processes)
        times.append(execution_time_parallel)
    print(times)
    return times

def plot_diff(size: int) -> None:
    """
        Plot the execution times of Kendall's Tau calculations with varying processes.

        Args:
           size: The number of data points for which to calculate and visualize execution times.
   """
    times = calculates_times(size)
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 9), times[1:], marker='o')
    plt.title('Kendall Correlation Speedup')
    plt.xlabel('Number of Processes')
    plt.ylabel('Speedup')
    plt.grid(True)
    plt.savefig('speedup.png')
    plt.show()

if __name__ == '__main__':
    freeze_support()
    plot_diff(size=10000)
