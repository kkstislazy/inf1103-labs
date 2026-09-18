FROM python:3.13.3

WORKDIR /app

COPY modular_auditor.py .

CMD ["python", "modular_auditor.py"]