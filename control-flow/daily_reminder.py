# Get task details from the user
task = input("Please enter a task description: ")
priority = input("Please enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority.lower():
    case "high":
        reminder = f"Urgent! Your task: '{task}' is of high priority."
    case "medium":
        reminder = f"Reminder: Your task: '{task}' is of medium priority."
    case "low":
        reminder = f"Note: Your task: '{task}' is of low priority."
    case _:
        reminder = "Invalid priority level entered."

# Check if the task is time-sensitive
if time_bound.lower() == "yes":
    reminder += " That requires immediate attention today!"

# Print the final reminder
print(reminder)
