from env.models import Observation

# EASY TASK
def easy_task():
    return Observation(
        patient_id=1,
        age=25,
        symptoms=["cold", "cough"],
        heart_rate=75,
        bp="120/80"
    ), "low"


# MEDIUM TASK
def medium_task():
    return Observation(
        patient_id=2,
        age=50,
        symptoms=["fever", "fatigue"],
        heart_rate=95,
        bp="135/85"
    ), "high"


# HARD TASK
def hard_task():
    return Observation(
        patient_id=3,
        age=65,
        symptoms=["chest pain", "shortness of breath"],
        heart_rate=120,
        bp="150/95"
    ), "emergency"