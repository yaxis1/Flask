FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    openjdk-11-jdk \
    wget \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /theapp

COPY . /theapp

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 2103

ENTRYPOINT ["python3"]

CMD ["run.py"]