import os
from openai import OpenAI
from env.environment import MedicalTriageEnv
from env.models import Action
from tasks.triage_tasks import easy_task, medium_task, hard_task
from graders.triage_grader import grade_action

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_prediction(observation):
    prompt = f"""
    You are a medical triage assistant.

    Patient details:
    Age: {observation.age}
    Symptoms: {observation.symptoms}
    Heart Rate: {observation.heart_rate}
    Blood Pressure: {observation.bp}

    Classify urgency into one of:
    low, medium, high, emergency

    Only return the label.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip().lower()


def run_task(task_func):
    env = MedicalTriageEnv()
    env.reset()

    observation, correct = task_func()
    env.state_data = observation

    print("\nPatient case:", observation)

    # AI prediction
    predicted = get_prediction(observation)

    action = Action(triage_level=predicted)

    _, reward, _, _ = env.step(action)

    score = grade_action(predicted, correct)

    print("Predicted:", predicted)
    print("Correct:", correct)
    print("Score:", score)

    return score


def main():
    total = 0

    print("Running Easy Task")
    total += run_task(easy_task)

    print("\nRunning Medium Task")
    total += run_task(medium_task)

    print("\nRunning Hard Task")
    total += run_task(hard_task)

    print("\nFinal Score:", total / 3)


if __name__ == "__main__":
    main()
