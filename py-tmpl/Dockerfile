FROM python:3.9

RUN apt update && apt upgrade && apt install -y libgl1-mesa-dev
WORKDIR /workspace
COPY . /workspace
RUN pip install --upgrade pip && pip install -r requirements.txt

# for pytest
ENV PYTHONPATH="/workspace/"
