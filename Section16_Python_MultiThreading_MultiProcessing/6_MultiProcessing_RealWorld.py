import multiprocessing
import sys
import time
import math

''' Increase Max Nuumber of digits for integer conversion '''
sys.set_int_max_str_digits(10000) # Important

def calc_factorial(number):
  print(f"Computing Factorial of: {number}")
  result = math.factorial(number)
  print(f"Factorial of {number} is {result}")
  return result

if __name__ == "__main__":
    start_time = time.time()
    numbers = [500,600,700]

    with multiprocessing.Pool() as pool:
        results = pool.map(calc_factorial,numbers)

    end_time = time.time()

    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
