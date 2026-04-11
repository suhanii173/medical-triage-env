from env.models import Observation, Action, Reward

class MedicalTriageEnv:

    def __init__(self):
        self.state_data = None
        self.done = False

    def reset(self):
        self.state_data = Observation(
            patient_id=1,
            age=65,
            symptoms=["chest pain", "shortness of breath"],
            heart_rate=120,
            bp="150/95"
        )
        self.done = False
        return self.state_data

    def step(self, action: Action):
        correct = "emergency"

        # SAME LOGIC, JUST FIXED VALUES
        if action.triage_level == correct:
            reward_value = 0.9   
            self.done = True
        elif action.triage_level == "high":
            reward_value = 0.5   # ok
            self.done = True
        else:
            reward_value = 0.1  

        # 🔒 SAFETY CLAMP (VERY IMPORTANT)
        reward_value = max(0.01, min(reward_value, 0.99))

        reward = reward_value

        return self.state_data, reward, self.done, {
            "correct": action.triage_level == correct
        }

    def state(self):
        return self.state_data
