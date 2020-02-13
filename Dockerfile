FROM python:alpine3.7
USER root
COPY . /news-api-scraper
WORKDIR /news-api-scraper
RUN pip install -r requirements.txt
RUN chmod 777 -R ./src config.cfg
CMD python ./src/__init__.py