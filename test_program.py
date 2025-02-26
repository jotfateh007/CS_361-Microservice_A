import subprocess

def call_microservice(category):
    result = subprocess.run(
        ["python", "microservice_A.py"],
        input=category,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

if __name__ == "__main__":
    categories = ["exercise", "study", "work"]
    for category in categories:
        print(f"Testing category: {category}")
        response = call_microservice(category)
        print(f"Response: {response}\n")