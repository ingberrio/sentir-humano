FROM python:3.10.4
COPY . /sentir
WORKDIR /sentir
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN python3 -m venv /opt/venv
COPY . .
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate
ENV secret_key=21nbd3$ef+jmvr6$3dku0fwgke1*2%2^8+fzlc7r#tktya*n@d
CMD gunicorn sentir.wsgi:application --bind 0.0.0.0:8888