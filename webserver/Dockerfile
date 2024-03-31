FROM python:3.9-alpine

WORKDIR /app

COPY /app/index.html .
COPY server.py .

EXPOSE 8080

CMD ["python", "server.py"]