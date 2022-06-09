FROM python:3.7
WORKDIR /usr/src/api
COPY requirements.txt .
RUN pip install --no-cache-dir SQLAlchemy==1.4.36
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002


COPY . .

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "5002"]
