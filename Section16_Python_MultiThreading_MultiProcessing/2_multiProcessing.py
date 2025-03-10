import multiprocessing
import time


def print_squares():
    for num in range(1, 4, 1):
        time.sleep(1)
        print(f"square of {num}: {num * num}")
def print_cubes():
    for num in range(1, 4, 1):
        time.sleep(1)
        print(f"cube of {num}: {num * num * num}")


if __name__ == "__main__":
  start = time.time()

  p1 = multiprocessing.Process(target = print_squares)
  p2 = multiprocessing.Process(target = print_cubes)

  p1.start()
  p2.start()

  # Wait for processes to complete
  p1.join()
  p2.join()

  finishedTime = time.time() - start
  print(finishedTime)