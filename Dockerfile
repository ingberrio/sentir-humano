FROM python:3.8.3-slim
COPY . /sentir
WORKDIR /sentir
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN python3 -m venv /opt/venv
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
CMD ["python3", "main.py"]
ENV secret_key=abc123
