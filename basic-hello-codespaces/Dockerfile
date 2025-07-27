FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .
COPY app.py .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt  
# Expose the port the app runs on
EXPOSE 1205

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "1205"]