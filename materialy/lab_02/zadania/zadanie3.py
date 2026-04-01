import multiprocessing
import time
from materialy.lab_02.zadania.lab2_functions import calculate_power_sum

if __name__ == "__main__":
    czas = time.time()
    zakres = range(1, 10001)

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(calculate_power_sum, zakres)
    
    print(time.time() - czas)
    pass