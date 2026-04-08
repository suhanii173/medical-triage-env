FROM python:3.10

WORKDIR /app

COPY . /app

RUN ls -la

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "inference.py"]
