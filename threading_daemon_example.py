import threading
import time

# Define a long-running task
def long_task():
    while True:
        print("Long task running...")
        time.sleep(2)

# Define a short task
def short_task():
    for i in range(5):
        print(f"Short task iteration {i + 1}")
        time.sleep(1)
    print("Short task complete!")

# Create threads
long_task_thread = threading.Thread(target=long_task, daemon=True)
short_task_thread = threading.Thread(target=short_task, daemon=True)

# Start the threads
long_task_thread.start()
short_task_thread.start()

# Wait for the short task to complete
short_task_thread.join()

# After the short task finishes, the program ends, and the daemon threads stop automatically
print("Main program exiting...")



#import threading
#import time

# Shared variable to control when the long task should stop
#stop_thread = False

# Define a long-running task that checks for stop condition
#def long_task():
#    while not stop_thread:
#        print("Long task running...")
#        time.sleep(2)
#    print("Long task stopped.")

# Define a short task
#def short_task():
#    global stop_thread
#    for i in range(5):
#        print(f"Short task iteration {i + 1}")
#       time.sleep(1)
#   stop_thread = True  # Stop the long task after short task finishes
#    print("Short task complete!")

# Create threads
#long_task_thread = threading.Thread(target=long_task, daemon=True)
#short_task_thread = threading.Thread(target=short_task, daemon=True)

# Start the threads
#long_task_thread.start()
#short_task_thread.start()

# Wait for the short task to complete
#short_task_thread.join()

# After the short task finishes, the main program ends, and the daemon threads stop automatically
#print("Main program exiting...")

