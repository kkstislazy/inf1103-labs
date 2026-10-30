FROM python:3.13.3

WORKDIR /app

COPY main.py .
COPT product.py .
COPY inventory.py .

CMD ["python", "inventory_manager.py"]