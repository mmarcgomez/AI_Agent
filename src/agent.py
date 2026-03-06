from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("'OPENAI_API_KEY' not found")

client = OpenAI(api_key=api_key)



def generate_plan(tasks):
    tasks_text = ""

    for t in tasks:
        tasks_text += f"- {t['task']} (deadline {t['deadline_days']} días, duración {t['duration']}h)\n"

    prompt = f"""
    You are an assistant that helps organize tasks.

    These are the tasks:

    {tasks_text}

    Please:
    1. Prioritize the tasks.
    2. Create a weekly plan from Monday to Friday.
    3. Briefly explain the reasoning.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[  # type: ignore
            {"role": "system", "content": "You are a task planning assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content