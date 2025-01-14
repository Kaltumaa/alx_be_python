def main():
    """Provide a customized reminder based on the task's priority and time sensitivity."""
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder variable
    reminder = ""

    # Replace match-case with if-elif for compatibility
    if priority == "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    elif priority == "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    elif priority == "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    else:
        print("Invalid priority level entered.")
        return  

    if time_bound == "yes":
        reminder += " that requires immediate attention today!" 
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity.")
        return 

    # Output the reminder
    print(reminder)

if __name__ == "__main__":
    main()
