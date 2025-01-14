def main():
    """Provide a customized reminder based on the task's priority and time sensitivity."""
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message
    reminder = ""

    # Match Case for priority levels
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            print("Invalid priority level entered.")
            return  # Exit the function if invalid priority is entered

    # Modify the reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity.")
        return  # Exit the function if invalid time-bound input is entered

    # Print the customized reminder
    print(reminder)


if __name__ == "__main__":
    main()
