from env.environment import MedicalTriageEnv
from env.models import Action

env = MedicalTriageEnv()

obs = env.reset()
print("Observation:", obs)

action = Action(triage_level="emergency")
obs, reward, done, info = env.step(action)

print("Reward:", reward)
print("Done:", done)
print("Info:", info)