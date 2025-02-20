import time
import threading

def print_numbers():
  for num in [1,2,3,4]:
    time.sleep(2)
    print(f"num: {num}")

def print_letter():
  for letter in "abc":
    time.sleep(2)
    print(f"letter: {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)
# Threading Reduces Time Significantly
start = time.time()
# Start Thread
t1.start()
t2.start()

# Wait for thread to complete
t1.join()
t2.join()

finish = time.time() - start
print(finish)

