import random
import time
from typing import Callable, Any

def exponential_backoff(
    func: Callable[..., Any],
    retries: int = 3,
    initial_delay: float = 2,
    backoff_factor: float = 2,
    max_delay: float = 32,
    jitter_factor: float = 0.3,
    **kwargs
) -> Any:
    """
    Executes a function with exponential backoff retry logic.

    Args:
        func (Callable): The function to execute.
        retries (int): Maximum number of retries. Default is 3.
        initial_delay (float): Initial delay in seconds. Default is 2.
        backoff_factor (float): Factor by which delay increases. Default is 2.
        max_delay (float): Maximum delay in seconds. Default is 32.
        jitter_factor (float): Jitter range (0.3 = ±30%). Default is 0.3.
        **kwargs: Arguments to pass to the function.

    Returns:
        Any: The result of the function if successful.

    Raises:
        Exception: If all retries fail, the last exception is raised.
    """
    delay = initial_delay
    for i in range(retries):
        try:
            return func(**kwargs)  # Execute the function with provided arguments
        except Exception as e:
            if i == retries - 1:  # If this is the last retry, raise the exception
                raise e
            # Calculate jittered sleep time
            jitter = random.uniform(1 - jitter_factor, 1 + jitter_factor)
            sleep_time = min(delay * jitter, max_delay)  # Clamp to max_delay
            print(f"Error occurred ({str(e)}), retrying in {sleep_time:.1f} seconds...")
            time.sleep(sleep_time)
            delay = min(delay * backoff_factor, max_delay)  # Update delay with backoff