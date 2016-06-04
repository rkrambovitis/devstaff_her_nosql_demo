FROM alpine:latest

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    cython \
    build-base 
RUN pip install cassandra-driver
RUN rm -rf /var/cache/apk/*

RUN mkdir -p /demo
COPY dsp.py dsg.py run.sh /demo/
WORKDIR /demo
COPY input_file .

#CMD ["/env/bin/python", "main.py"]
ENTRYPOINT ["/demo/run.sh"]
