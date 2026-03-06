import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = "https://router.huggingface.co/hf-inference/models/HuggingFaceH4/zephyr-7b-beta"
API_KEY = os.getenv("HF_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def generate_plan(tasks):

    tasks_text = ""

    for t in tasks:
        tasks_text += f"- {t['task']} (deadline {t['deadline_days']} days, duration {t['duration']}h)\n"

    prompt = f"""
        You are an assistant that organizes tasks.
        
        These are the tasks:
        
        {tasks_text}
        
        1. Prioritize the tasks.
        2. Create a weekly plan from Monday to Friday.
        3. Briefly explain the decision.
        """

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("STATUS:", response.status_code)
    print("RAW RESPONSE:", response.text)

    result = response.json()

    return result[0]["generated_text"]