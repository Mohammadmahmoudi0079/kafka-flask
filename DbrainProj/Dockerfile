FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8001

STOPSIGNAL SIGINT

ENTRYPOINT ["python"]
CMD ["rest_api.py"]
