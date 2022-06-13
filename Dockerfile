FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1
## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY requirements.txt requirements.txt
RUN pip install pip &&\
    pip install -r requirements.txt 

COPY . app.py /app/
## Step 3:
# Install packages from requirements.txt


## Step 4:
# Expose port 80

EXPOSE 80
## Step 5:
# Run app.py at container launch

CMD ["python3", "app.py"]
	