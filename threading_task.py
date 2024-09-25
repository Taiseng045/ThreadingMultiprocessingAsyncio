import threading
import time

def simulate_io_task(file_name, duration):
  # pass
  with open(file_name,"r") as f:
    data = f.read()
  time.sleep(duration)
  print(f"Completed {file_name}")
def run_io_tasks():
  # pass
  files = ["index1.txt", "index2.txt", "index3.txt"]
  num_threads = len(files)

  threads = []
  for i in range(num_threads):
    file_name = files[i]
    thread = threading.Thread(target=simulate_io_task, args=(file_name, 2))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  print("I/O tasks completed.")
