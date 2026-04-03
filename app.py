import gradio as gr
from env.environment import MedicalTriageEnv
from env.models import Action, Observation

env = MedicalTriageEnv()

def run_triage(age, symptoms, heart_rate, bp):

    symptoms_list = [s.strip().lower() for s in symptoms.split(",")]

    obs = Observation(
        patient_id=1,
        age=age,
        symptoms=symptoms_list,
        heart_rate=heart_rate,
        bp=bp
    )

    env.state_data = obs

    # smarter logic
    if "chest pain" in symptoms_list or heart_rate > 110:
        pred = "🚨 EMERGENCY"
        score = 1.0
        reason = "Critical condition detected. Immediate medical attention required."
    elif "fever" in symptoms_list or heart_rate > 95:
        pred = "⚠️ HIGH"
        score = 0.8
        reason = "High-risk condition. Needs urgent care."
    elif "fatigue" in symptoms_list:
        pred = "🟡 MEDIUM"
        score = 0.5
        reason = "Moderate condition. Monitor closely."
    else:
        pred = "🟢 LOW"
        score = 0.2
        reason = "Low risk. Basic care sufficient."

    return pred, score, reason


with gr.Blocks() as demo:
    
    gr.Markdown("# 🏥 AI Medical Triage System")
    gr.Markdown("### Simulating real-world hospital emergency prioritization using AI")

    with gr.Row():
        with gr.Column():
            age = gr.Number(label="👤 Age")
            symptoms = gr.Textbox(label="🩺 Symptoms (comma separated)", placeholder="e.g. chest pain, fever")
            heart_rate = gr.Number(label="❤️ Heart Rate")
            bp = gr.Textbox(label="🩸 Blood Pressure")

            submit = gr.Button("🔍 Analyze Patient", variant="primary")

        with gr.Column():
            output1 = gr.Textbox(label="🚦 Triage Level")
            output2 = gr.Textbox(label="📊 Risk Score")
            output3 = gr.Textbox(label="🧠 Explanation")

    submit.click(
        fn=run_triage,
        inputs=[age, symptoms, heart_rate, bp],
        outputs=[output1, output2, output3]
    )

demo.launch()