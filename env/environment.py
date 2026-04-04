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

        # YOUR ORIGINAL LOGIC (unchanged)
        if action.triage_level == correct:
            reward_value = 1.0
            self.done = True
        elif action.triage_level == "high":
            reward_value = 0.5
            self.done = True
        else:
            reward_value = -0.2

        # NEW: Wrap into Reward model (OpenEnv requirement)
        reward = Reward(score=reward_value)

        return self.state_data, reward, self.done, {
            "correct": action.triage_level == correct
        }

    def state(self):
        return self.state_data