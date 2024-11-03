# Your task
# Create a Python script that allows users to repeatedly start and stop a timer for given tasks.

# After each task is completed, the script will print the duration of the task, then ask for the next task name.

# If the user enters "exit" instead of a task name, the script will stop and print a summary of all tasks and their respective durations.

# Refer to the example output below to see how the script is to be used.

# Guidelines
# Use time.time() to capture the start and end times of tasks.
# This functions returns a timestamp - a number that represents each moment in time, and increases by 1 in each second.
# Example:
# import time

# now = time.time()
# Calculate the elapsed time for each task and store it in a dictionary.
# After the user has finished timing tasks, print a summary of all tasks and their durations.
# Example output
# Enter the task name to start (or 'exit' to stop): Writing report
# Starting task 'Writing report'...
# Press Enter to stop the task... 
# Task 'Writing report' completed in 42.95 seconds.

# Enter the task name to start (or 'exit' to stop): Reading
# Starting task 'Reading'...
# Press Enter to stop the task... 
# Task 'Reading' completed in 113.39 seconds.

# Enter the task name to start (or 'exit' to stop): exit

# All tasks and their durations:
# Writing report: 42.95 seconds
# Reading: 113.39 seconds

import time

now = time.time()
all_tasks = {}

while True:
    input_taken = input("Enter the task name to start (or 'exit' to stop): ")

    if input_taken != "exit":  # ensure that user does not want to exit
        print(f"Starting task '{input_taken}'...")
        enter = input("Press Enter to stop the task... ")

        if not enter:
            elapsed = time.time()
            completion_time = round(elapsed - now,2)
            all_tasks[input_taken] = completion_time
            print(f"Task '{input_taken}' completed in {completion_time} seconds.")

    else:
        print("All tasks and their durations: ")
        for key, value in all_tasks.items():
            print(f"{key}: {value} seconds")
        break
