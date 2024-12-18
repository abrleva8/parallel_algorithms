# Kendall's Tau Calculation

This project implements the Kendall's Tau statistic to measure the correlation between two variables. The implementation includes both single-threaded and multi-threaded approaches using the Python `multiprocessing` module. This allows for efficient computation of Kendall's Tau for larger datasets.

## Features

- Generate random datasets of floating-point numbers.
- Calculate Kendall's Tau using:
  - A single-threaded approach.
  - A multi-threaded approach using multiple processes.
- Measure and compare the execution time of both approaches.
- Visualize the speedup achieved through parallel processing.

## Algorithms Used

### Kendall's Tau

Kendall's Tau is a non-parametric statistic that measures the ordinal association between two variables. It assesses how well the relationship between two variables can be described using a monotonic function. The algorithm operates as follows:

1. **Pairwise Comparison**: For each pair of items, determine if they are concordant or discordant:
   - **Concordant Pair**: A pair $(x_i, y_i)$ and $(x_j, y_j)$ is concordant if the ranks for $x_i$ and $x_j$ are in the same order as the ranks for $y_i$ and $y_j$, i.e., if $(x_i - x_j)(y_i - y_j) > 0$.
   - **Discordant Pair**: A pair is discordant if the ranks for $x$ are in the opposite order to the ranks for $y$, i.e., if $(x_i - x_j)(y_i - y_j) < 0$.

2. **Count Pairs**: Count the total number of concordant and discordant pairs.

3. **Calculate Tau**: Kendall's Tau $\tau$ is computed using the formula:
   $\tau = \frac{2(C - D)}{n(n - 1)}$
   where $C$ is the number of concordant pairs, $D$ is the number of discordant pairs, and $n$ is the number of observations.

### Implementation

- **Single-Threaded Approach**: The implementation involves nested loops that traverse through the dataset to compare each pair of points for concordance or discordance. This is straightforward but can be inefficient for large datasets.
  
- **Multi-Threaded Approach**: The multi-threaded implementation utilizes Python’s `multiprocessing` module to distribute the work across several processes. Each process independently counts concordant and discordant pairs for a portion of the dataset. The results from all processes are then aggregated to compute the final Kendall's Tau statistic.

## Requirements

To run this project, you will need:

- Python 3.x
- `matplotlib` for plotting graphs (can be installed via `pip`)
- Standard Python libraries such as `random`, `time`, and `multiprocessing`.

You can install the required libraries using pip:

```bash
pip install matplotlib
```
## Getting Started

1. Clone the repository to your local machine:

   git clone https://github.com/abrleva8/parallel_algorithms.git

2. Change to the project directory:

   cd parallel_algorithms

3. Run the script to generate data, calculate Kendall's Tau, and visualize the results:

   python main.py

   Replace main.py with the actual filename if different.

## Code Structure

- `create_data(size)`: Generates two lists of random floating-point numbers of length size.
- `timing_decorator(func)`: A decorator that measures execution time of the provided function.
- `count_concordant_discordant(i, x, y)`: Counts concordant and discordant pairs for a given index.


- `kendall_tau_multi_thread(x, y, num_processes)`: Calculates Kendall's Tau using a multi-threaded approach.
- `kendall_tau_single_thread(x, y)`: Calculates Kendall's Tau using a single-threaded approach.
- `calculates_times(size)`: Computes execution times for different numbers of processes.
- `plot_diff(size)`: Plots execution times and visualizes the correlation speedup.

## Example Output

Upon running the script, you will obtain a plot named `speedup.png`, which visually represents the speedup achieved when using multiple processes as opposed to a single-threaded approach.

![image](https://github.com/user-attachments/assets/bb08b11c-0710-4019-bf9b-b494c5d0524d)


