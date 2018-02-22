FROM python:2.7.10

RUN mkdir -p /stacks
WORKDIR /stacks
COPY setup.py /stacks

RUN python setup.py install

COPY . /stacks

RUN python setup.py install > /dev/null
