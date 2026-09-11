FROM python:3.13.3

WORKDIR /app

COPY auditor.py .

CMD ["python", "auditor.py"]