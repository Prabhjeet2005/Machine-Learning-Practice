from concurrent.futures import ProcessPoolExecutor
import time

def print_squares(number):
  time.sleep(1)
  print(f"square: {number * number}")

if __name__ == "__main__":
  numbers = [1,2,3,4,5,6,7,8,9,90]
  with ProcessPoolExecutor(max_workers=2) as executor:
    results = executor.map(print_squares,numbers)