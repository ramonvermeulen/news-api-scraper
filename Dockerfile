FROM python:alpine3.7
USER root
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
RUN chmod 777 -R ./src config.cfg
CMD python ./src/__init__.py