import random

MESSAGE_FILES = {
    "exercise": "exercise_messages.txt",
    "study": "study_messages.txt",
    "work": "work_messages.txt"
}

def load_messages(category):
    if category not in MESSAGE_FILES:
        return None
    try:
        with open(MESSAGE_FILES[category], "r") as file:
            messages = file.readlines()
        return [msg.strip() for msg in messages]
    except FileNotFoundError:
        return None

def get_random_message(category):
    messages = load_messages(category)
    if not messages:
        return "Invalid category or no messages found."
    return random.choice(messages)

def microservice(category):
    return get_random_message(category)

if __name__ == "__main__":
    category = input("Enter category (exercise, study, work): ").strip().lower()
    print(microservice(category))