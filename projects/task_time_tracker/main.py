#
'''
This program prompt the user to enter task name, time spent to finish it,
calculate total spent time on all performed tasks, and display which task
take more time on the console.
'''
# Declare global variables to store data
total_time_spent = 0.0
most_consuming_task = ''
tasks = {}

while True:
    # 1. Ask the user to enter a task name
    print()
    task_name = input("Enter task name or 'done' to exit the program: ")

    # Check if the user decided to exit the program
    if task_name.lower() == 'done':
        print("You have decided to exit the program.")
        break

    # 2. Ask how many minutes they spent on it
    time_spent = float(input("How many minutes did you spend on it? "))

    # 3. Keep total of all time spent 
    # Add the new task to the dictionary list with its time spent on it
    tasks[task_name] = time_spent

    # Add the newly entered time spent to the total_time_spent
    total_time_spent += time_spent

# 4. Allow the user to see their most time-consuming task
# Go inside time_spent column and get the maximum value

# Initialize max_value with a very small number – negative infinity
max_value = float('-inf')

# Loop/Iterate through the dictionary (tasks) and find the maximum value
for key, value in tasks.items():
    if isinstance(value, float):
        if value > max_value:
            max_value = value
            most_consuming_task = key

print(f"Total time spent on all tasks: {total_time_spent} minutes")
print(f"The task that took the most time to perform is: '{most_consuming_task}' with {max_value} minutes")
