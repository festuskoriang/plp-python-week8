import random


# Lets the player guess a random number from 1 to 20.
def play_number_guessing_game():
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number from 1 to 20.")
    attempts = 0

    while True:
        guess_text = input("Your guess: ")
        try:
            guess = int(guess_text)
        except ValueError:
            print(f"'{guess_text}' isn't a whole number. Please try again.")
            continue

        attempts += 1
        if guess < secret_number:
            print(f"{guess} is too low. Try again!")
        elif guess > secret_number:
            print(f"{guess} is too high. Try again!")
        else:
            print(f"That's right! You guessed it in {attempts} tries.")
            return


# Calculates the result of adding, subtracting, multiplying, or dividing two numbers.
def run_calculator():
    try:
        first_number = float(input("First number: "))
        operation = input("Operation (+, -, *, /): ").strip()
        second_number = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You can't divide by zero.")
            return
        result = first_number / second_number
    else:
        print("Please choose +, -, *, or /.")
        return

    print(f"{first_number:g} {operation} {second_number:g} = {result:g}")


# Lets the user add, view, and clear tasks in a to-do list.
def manage_todo_list(tasks):
    print("To-do list: 1. Add a task  2. View tasks  3. Clear tasks")
    action = input("Choose an action (1-3): ").strip()

    if action == "1":
        task = input("Task to add: ").strip()
        if task:
            tasks.append(task)
            print(f"Added '{task}'. You now have {len(tasks)} task(s).")
        else:
            print("An empty task wasn't added.")
    elif action == "2":
        if tasks:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
        else:
            print("Your to-do list is empty.")
    elif action == "3":
        tasks.clear()
        print("To-do list cleared.")
    else:
        print("Please choose an action from 1 to 3.")


def main():
    tasks = []
    print("Welcome to My Toolkit! Choose a tool to get started.")

    while True:
        print("\n=== My Toolkit ===")
        print("1. Number guessing game")
        print("2. Simple calculator")
        print("3. To-do list")
        print("4. Quit")
        choice = input("Choose a tool (1-4): ").strip()

        if choice == "1":
            play_number_guessing_game()
        elif choice == "2":
            run_calculator()
        elif choice == "3":
            manage_todo_list(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' isn't on the menu. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()