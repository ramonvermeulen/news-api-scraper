FROM python:alpine3.7
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
RUN chmod -R 777 .
CMD python ./src/__init__.py