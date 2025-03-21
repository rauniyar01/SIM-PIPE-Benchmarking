FROM python:3.9-slim
RUN apt-get update && apt-get install -y libsm6 libxext6 && rm -rf /var/lib/apt/lists/*
RUN pip install opencv-python-headless psutil
WORKDIR /app
COPY filter.py /app/
CMD ["python", "filter.py"]
