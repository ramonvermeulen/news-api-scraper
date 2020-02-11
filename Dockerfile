FROM python:alpine3.7
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
RUN chmod 777 ./config.cfg
CMD python ./src/__init__.py