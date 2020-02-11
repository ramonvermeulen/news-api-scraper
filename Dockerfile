FROM python:alpine3.7
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
RUN chmod 777 ./config.cfg
CMD python ./src/__init__.py