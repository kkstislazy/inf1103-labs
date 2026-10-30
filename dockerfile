FROM python:3.13.3

WORKDIR /app

COPY main.py .
COPY product.py .
COPY inventory.py .

CMD ["python", "main.py"]