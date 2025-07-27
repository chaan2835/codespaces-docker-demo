FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY app.py .
RUN pip install --no-cache-dir -r requirements.txt  
EXPOSE 1205
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "1205"]
