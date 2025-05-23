FROM python:3.12.1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_RUN_PORT=5000

CMD ["flask", "run", "--host=0.0.0.0"]
