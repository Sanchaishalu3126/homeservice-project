FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p static/uploads

EXPOSE 5000

CMD ["python", "app.py"]