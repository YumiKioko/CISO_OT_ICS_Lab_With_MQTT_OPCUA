# Dockerfile for Snap7 attacker tools
FROM python:3.11
RUN pip install snap7
COPY . /attacker
WORKDIR /attacker
CMD ["python", "snap7_attack.py"]
