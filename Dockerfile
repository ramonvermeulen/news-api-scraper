FROM python:alpine3.7
USER root
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
RUN find ! -name proc|sys -exec chmod 755 {} \;
CMD python ./src/__init__.py