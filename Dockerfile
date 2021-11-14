FROM python:3.8.6-slim

# Dependencies and Config
##RUN useradd -ms /bin/bash bolivia

# Create user
#USER bolivia

# Working directory
#WORKDIR /home/bolivia

RUN mkdir /app

WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY . .