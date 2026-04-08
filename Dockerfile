FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

# FORCE install all needed packages
RUN pip install fastapi uvicorn openai gradio==4.0.0

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
