FROM python:3.13.3

WORKDIR /app

COPY persistent_auditor.py .

CMD ["python", "persistent_auditor.py"]