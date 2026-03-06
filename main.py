import os
from data.tasks import tasks
from src.agent_oll import generate_plan

try:
    plan = generate_plan(tasks)

    print(plan)

    os.makedirs("output", exist_ok=True)

    with open("output/weekly_planner.txt", "w", encoding="utf-8") as f:
        f.write(plan)

except Exception as e:
    print("No se pudo completar la solicitud. Error:", e)