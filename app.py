import sys
import os
sys.path.append(os.path.abspath("."))

import gradio as gr
from env.environment import MedicalTriageEnv

env = MedicalTriageEnv()


def run_triage(age, manual_symptoms, selected_symptoms, heart_rate, bp):

    #  Validation
    if age is None or age < 0 or age > 120:
        return "❌ ERROR", "0%", "Invalid age (0–120 only)", "0%"

    if heart_rate is None or heart_rate < 30 or heart_rate > 200:
        return "❌ ERROR", "0%", "Invalid heart rate (30–200 bpm)", "0%"

    if not bp or "/" not in bp:
        return "❌ ERROR", "0%", "Enter BP like 120/80", "0%"

    if not manual_symptoms and not selected_symptoms:
        return "❌ ERROR", "0%", "Enter or select symptoms", "0%"

    symptoms_list = []

    if manual_symptoms:
        symptoms_list += [s.strip().lower() for s in manual_symptoms.split(",")]

    if selected_symptoms:
        symptoms_list += [s.lower() for s in selected_symptoms]

    symptoms_text = " ".join(symptoms_list)

    score = 0
    reasons = []

   
    if any(word in symptoms_text for word in ["chest", "pressure", "tightness"]):
        score += 50
        reasons.append("Possible cardiac issue")

    if any(word in symptoms_text for word in ["breath", "breathing"]):
        score += 30
        reasons.append("Breathing difficulty")

    if any(word in symptoms_text for word in ["fever", "infection"]):
        score += 20
        reasons.append("Fever or infection")

    if any(word in symptoms_text for word in ["fatigue", "weakness"]):
        score += 10
        reasons.append("General weakness")

    if any(word in symptoms_text for word in ["dizziness", "headache"]):
        score += 10
        reasons.append("Neurological symptoms")

    #  Vitals
    if heart_rate > 110:
        score += 30
        reasons.append("High heart rate")
    elif heart_rate > 90:
        score += 15
        reasons.append("Elevated heart rate")

    if age > 60:
        score += 20
        reasons.append("Elderly patient")

    #  Decision
    if score >= 80:
        level = "🚨 EMERGENCY"
    elif score >= 50:
        level = "⚠️ HIGH"
    elif score >= 25:
        level = "🟡 MEDIUM"
    else:
        level = "🟢 LOW"

    #  Confidence 
    confidence = min(95, 50 + score // 2)

    explanation = "\n".join(reasons) if reasons else "No major risk factors."

    return level, f"{score}%", explanation, f"{confidence}%"



css = """
body {
    background: #000;
    color: #fff;
}
.gr-box {
    background: #111 !important;
    border-radius: 12px !important;
}
input, textarea {
    background: #222 !important;
    color: #fff !important;
    border-radius: 8px !important;
}
.gr-button {
    background: #222 !important;
    color: #fff !important;
    border-radius: 12px !important;
}
.gr-button:hover {
    background: #fff !important;
    color: #000 !important;
}
"""


with gr.Blocks(css=css) as demo:

    gr.Markdown("# 🏥 AI Medical Triage System")
    gr.Markdown(" Intelligent Patient Risk-Assesement(OpenEnv-based)")

    with gr.Row():

        # INPUT
        with gr.Column():
            gr.Markdown("### 👤 Patient Input")

            age = gr.Number(label="Age (0–120)", minimum=0, maximum=120)

            manual_symptoms = gr.Textbox(
                label="📝 Enter Symptoms",
                placeholder="chest pain, fever"
            )

            selected_symptoms = gr.CheckboxGroup(
                choices=[
                    "Chest Pain",
                    "Fever",
                    "Shortness of Breath",
                    "Fatigue",
                    "Headache",
                    "Dizziness"
                ],
                label="⚡ Or Select Symptoms"
            )

            heart_rate = gr.Number(label="❤️ Heart Rate (30–200)", minimum=30, maximum=200)

            bp = gr.Textbox(label="🩸 Blood Pressure (e.g. 120/80)")

            submit = gr.Button("🚀 Analyze Patient")

        # OUTPUT
        with gr.Column():
            gr.Markdown("### 📊 Triage Result")

            output1 = gr.Textbox(label="🚦 Triage Level")
            output2 = gr.Textbox(label="📊 Risk Score")
            output3 = gr.Textbox(label="🧠 Explanation")
            output4 = gr.Textbox(label="🤖 AI Confidence")

    submit.click(
        fn=run_triage,
        inputs=[age, manual_symptoms, selected_symptoms, heart_rate, bp],
        outputs=[output1, output2, output3, output4]
    )

    gr.Markdown("⚠️ *Simulation only. Not real medical advice.*")


if __name__ == "__main__":
    demo.launch()
 