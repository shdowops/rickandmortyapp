FROM python:3.6

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 3000

CMD [ "python", "./app.py" ]
