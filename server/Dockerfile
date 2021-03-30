FROM python:3

WORKDIR /app

ENV FLASK_APP=app.py 

ENV FLASK_ENV=development

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]

