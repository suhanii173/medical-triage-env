
# 🏥 AI Medical Triage Environment (OpenEnv)

## 📌 Overview

This project implements a real-world **medical triage simulation environment** using the OpenEnv framework.
It allows AI agents to learn how to prioritize patients based on symptoms and vital signs.

Medical triage is a critical process used in hospitals to determine which patients need immediate attention.

---

## 🎯 Objective

To simulate real-world emergency decision-making where an AI agent:

* Observes patient data
* Predicts urgency level
* Gets rewarded based on correctness

---

## 🧠 Environment Design

### Observation Space

Each patient includes:

* Age
* Symptoms
* Heart Rate
* Blood Pressure

---

### Action Space

The agent predicts one of:

* low
* medium
* high
* emergency

---

### Reward Function

* Correct classification → **1.0**
* Partially correct → **0.5**
* Incorrect → **-0.2**

This provides continuous feedback and encourages better learning.

---

## 🧪 Tasks

### 🟢 Easy

* Mild symptoms (cold, cough)
* Expected: low

### 🟡 Medium

* Fever, fatigue
* Expected: high

### 🔴 Hard

* Chest pain, breathing issues
* Expected: emergency

---

## 🤖 Baseline Agent

A simple rule-based agent is implemented in `inference.py`.

It produces reproducible scores across all tasks.

---

## 🖥️ API Endpoints

* `/reset` → Initializes environment
* `/step` → Takes action and returns result

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python inference.py
```

To run UI:

```bash
python app.py
```

---

## 🐳 Docker Support

The project includes a Dockerfile for containerized deployment.

---

## 🌐 Deployment

Deployed using Hugging Face Spaces with OpenEnv compatibility.

---

## 💡 Motivation

This project demonstrates how AI agents can be trained for real-world healthcare decision-making tasks.

---

## 👤 Author

Suhani

