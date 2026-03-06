import ollama


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

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are an expert task planner."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
