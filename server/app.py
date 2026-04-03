from fastapi import FastAPI
import uvicorn
from env.environment import MedicalTriageEnv
from env.models import Action

app = FastAPI()

env = MedicalTriageEnv()

@app.get("/")
def home():
    return {"message": "Medical Triage Environment Running"}

@app.get("/reset")
def reset():
    obs = env.reset()
    return obs

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)
    return {
        "observation": obs,
        "reward": reward.score,
        "done": done,
        "info": info
    }

#  REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

#  REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()