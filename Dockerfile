FROM python:3.9

RUN pip install --upgrade pip
RUN pip install numpy pandas scikit-learn nltk

RUN mkdir /app
WORKDIR /app

COPY . .

CMD ["python", "mypy.py"]
