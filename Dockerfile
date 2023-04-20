FROM python:3.10.9-slim
MAINTAINER Steven Skoczen <steven@oxintel.ai>

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    gfortran


RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the bot.py script
CMD ["python", "bot.py"]
