import time
import numpy as np
from scipy import stats

def time_complexity_estimator(func, generator, sizes, repetitions=3,small_time_threshold=1e-9):
   
    times = []

    # Measure the execution time for each input size
    for size in sizes:
        inputs = generator(size)
        duration = []
        
        for _ in range(repetitions):
            start_time = time.time()
            func(inputs)
            end_time = time.time()
            duration.append(end_time - start_time)
        
        avg_time = np.mean(duration)

        if avg_time < small_time_threshold:
            avg_time = small_time_threshold


        times.append(avg_time)
        print(f"Input size: {size}, Avg execution time: {avg_time:.6f} seconds")
    
    # Perform logarithmic transformation to test for different complexity models
    log_sizes = np.log(sizes)
    log_times = np.log(times)

    
    # Perform linear regression (O(n)) - Time complexity as a function of size
    slope, intercept, r_value, p_value, std_err = stats.linregress(sizes, times)
    linear_fit = [slope * size + intercept for size in sizes]
    
    # Perform quadratic fit (O(n^2))
    quadratic_fit = [slope * size**2 + intercept for size in sizes]
    
    # Perform logarithmic fit (O(log n))
    log_fit = [slope * np.log(size) + intercept for size in sizes]

    def r_squared(actual, fit):
        residuals = np.subtract(actual, fit)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((actual - np.mean(actual))**2)
        return 1 - (ss_res / ss_tot)

    r_linear = r_squared(times, linear_fit)
    r_quadratic = r_squared(times, quadratic_fit)
    r_log = r_squared(times, log_fit)

    # Print R-squared values for each fit
    print(f"R-squared for O(n): {r_linear:.4f}")
    print(f"R-squared for O(n^2): {r_quadratic:.4f}")
    print(f"R-squared for O(log n): {r_log:.4f}")
    
    # Determine the best fit based on highest R-squared
    if r_linear > r_quadratic and r_linear > r_log:
        return "O(n)"
    elif r_quadratic > r_linear and r_quadratic > r_log:
        return "O(n^2)"
    elif r_log > r_linear and r_log > r_quadratic:
        return "O(log n)"
    else:
        return "Unknown (complexity is not easily determined)"

if __name__ == "__main__":
    def example_function(data):
        return sum(data)

    def input_generator(size):
        return list(range(size))

    # Define input sizes to test
    input_sizes = [10, 100, 1000, 10000, 50000, 100000]

    # Estimate time complexity
    estimated_complexity = time_complexity_estimator(example_function, input_generator, input_sizes)
    print(f"Estimated Time Complexity: {estimated_complexity}")


