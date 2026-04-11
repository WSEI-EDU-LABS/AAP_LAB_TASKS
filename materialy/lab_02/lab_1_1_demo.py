#Stwórz dekorator timer, który będzie mierzył czas wykonania funkcji 
#i wyświetlał go po zakończeniu jej działania.
import time
import functools
import logging 

logging.basicConfig(level=logging.INFO)

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"""Function '{func.__name__}' execution time: {execution_time:.5f} seconds""")
        return result
    return wrapper

@timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = example_function(1000000)
print("Result:", result)




