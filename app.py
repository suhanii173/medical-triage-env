import sys
import os
sys.path.append(os.path.abspath("."))

import gradio as gr
from env.environment import MedicalTriageEnv
from env.models import Observation

env = MedicalTriageEnv()

# 🔥 Improved scoring-based triage logic
def run_triage(age, symptoms, heart_rate, bp):

    symptoms_list = [s.strip().lower() for s in symptoms.split(",")]

    score = 0
    reasons = []

    # 🧠 Smart scoring
    if "chest pain" in symptoms_list:
        score += 50
        reasons.append("Chest pain detected (high cardiac risk)")
    if "shortness of breath" in symptoms_list:
        score += 30
        reasons.append("Breathing difficulty detected")
    if "fever" in symptoms_list:
        score += 20
        reasons.append("Fever present (possible infection)")
    if "fatigue" in symptoms_list:
        score += 10
        reasons.append("Fatigue observed")

    if heart_rate > 110:
        score += 30
        reasons.append("High heart rate")
    elif heart_rate > 90:
        score += 15
        reasons.append("Elevated heart rate")

    if age > 60:
        score += 20
        reasons.append("Elderly patient (higher risk)")

    # 🚦 Classification
    if score >= 80:
        level = "🚨 EMERGENCY"
        color = "red"
    elif score >= 50:
        level = "⚠️ HIGH"
        color = "orange"
    elif score >= 25:
        level = "🟡 MEDIUM"
        color = "gold"
    else:
        level = "🟢 LOW"
        color = "green"

    explanation = "\n".join(reasons) if reasons else "No major risk factors detected."

    return level, score, explanation


# 🎨 UI DESIGN
with gr.Blocks() as demo:

    gr.Markdown("""
    # 🏥 Medical Triage Simulation System
    ### ⚡ Intelligent Patient Risk Assessment (OpenEnv-based)
    ---
    """)

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 👤 Patient Information")

            age = gr.Number(label="Age", value=30)
            symptoms = gr.Textbox(
                label="Symptoms (comma separated)",
                placeholder="e.g. chest pain, fever"
            )
            heart_rate = gr.Number(label="Heart Rate (bpm)", value=80)
            bp = gr.Textbox(label="Blood Pressure", value="120/80")

            submit = gr.Button("🔍 Analyze Patient", variant="primary")

        with gr.Column():
            gr.Markdown("### 📊 Triage Result")

            output1 = gr.Textbox(label="Triage Level")
            output2 = gr.Number(label="Risk Score")
            output3 = gr.Textbox(label="Explanation")

    # 🔗 Connect button
    submit.click(
        fn=run_triage,
        inputs=[age, symptoms, heart_rate, bp],
        outputs=[output1, output2, output3]
    )

if __name__ == "__main__":
    demo.launch()
