from env.environment import MedicalTriageEnv
from env.models import Action
from tasks.triage_tasks import easy_task, medium_task, hard_task
from graders.triage_grader import grade_action


def run_task(task_func):
    env = MedicalTriageEnv()
    
    observation, correct = task_func()
    
    env.state_data = observation  # load task into env
    
    print("\nPatient case:", observation)

    # BASELINE AGENT (simple logic)
    if "chest pain" in observation.symptoms:
        predicted = "emergency"
    elif "fever" in observation.symptoms:
        predicted = "high"
    else:
        predicted = "low"

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