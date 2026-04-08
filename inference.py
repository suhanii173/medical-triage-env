import os
import requests
from openai import OpenAI

# 🔑 REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

# 🤖 OpenAI client (MANDATORY by rules)
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

# 🔗 YOUR HF SPACE URL
BASE_URL = "https://slyslia-medical-triage-system.hf.space"


# 🧠 Simple decision logic (baseline agent)
def decide_action(obs):
    symptoms = " ".join(obs.get("symptoms", [])).lower()
    hr = obs.get("heart_rate", 0)

    if "chest" in symptoms or "breath" in symptoms or hr > 110:
        return "emergency"
    elif "fever" in symptoms:
        return "high"
    elif "fatigue" in symptoms:
        return "medium"
    else:
        return "low"


def run_episode(task_name):
    print(f"[START] task={task_name} env=medical-triage model={MODEL_NAME}")

    rewards = []
    step_count = 0
    success = False

    try:
        # 🔄 RESET
        res = requests.get(f"{BASE_URL}/reset")
        obs = res.json()

        done = False

        while not done and step_count < 5:
            step_count += 1

            action = decide_action(obs)

            # 🔁 STEP
            response = requests.post(
                f"{BASE_URL}/step",
                json={"triage_level": action}
            ).json()

            reward = float(response["reward"])
            done = response["done"]
            error = None

            rewards.append(f"{reward:.2f}")

            print(
                f"[STEP] step={step_count} action={action} "
                f"reward={reward:.2f} done={str(done).lower()} error={error}"
            )

            obs = response["observation"]

            if done:
                success = True

    except Exception as e:
        error = str(e)
        print(
            f"[STEP] step={step_count} action=null "
            f"reward=0.00 done=true error={error}"
        )
        success = False

    print(
        f"[END] success={str(success).lower()} "
        f"steps={step_count} rewards={','.join(rewards)}"
    )


# 🚀 RUN 3 TASKS (REQUIRED)
if __name__ == "__main__":
    run_episode("easy")
    run_episode("medium")
    run_episode("hard")