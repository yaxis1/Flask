FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /theapp

COPY . /theapp

RUN pip3 --no-cache-dir install -r requirements.txt
RUN python3 
RUN from flaskapp import db
RUN db.create_all()

EXPOSE 2103

ENTRYPOINT ["python3"]
CMD ["run.py"]




