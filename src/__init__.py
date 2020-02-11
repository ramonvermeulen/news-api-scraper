import configparser
import schedule
import time
import datetime
from mailer import Mailer
from api_provider import APIProvider
import json
import logging
import sys


def job(http_provider, mail_provider):
    try:
        res = http_provider.fetch_data()
        data = res[0]
        failed_counter = res[1]
        if failed_counter != 0 and failed_counter % 10 == 0:
            mail_provider.send_mail(f'RAMON CHECK JE SERVER', f'''
                CHECK FF JE SERVER WANT: failed_counter={failed_counter}
            ''')
        latest_update = get_datetime_from_file()
        for record in data.get('articles'):
            datetime_instance = datetime.datetime.fromisoformat(record.get('publishedAt').replace('Z', ''))
            if datetime_instance > latest_update:
                mail_provider.send_mail(f'Alfen News! - {record.get("title")}', f'''
                    {record.get('title')}\n{record.get('url')}\n{record.get('publishedAt')}\n{record.get('description')}
                ''')
    except Exception as e:
        logging.exception(f'[{datetime.datetime.now()}] - Error during job')


def write_timestamp_to_file(datetime_instance):
    ts_file = open('../last_news_update', 'w')
    ts_file.write(datetime_instance.isoformat())
    ts_file.close()


def get_datetime_from_file():
    ts_file = open('../last_news_update', 'r')
    line = ts_file.readline()
    ts_file.close()
    return datetime.datetime.fromisoformat(line)


def get_config(key='MAIN'):
    config_parser = configparser.ConfigParser()
    config_parser.read('../config.cfg')
    return config_parser[key]


def setup_scheduler():
    config = get_config()
    mail_config = get_config('MAIL')
    http_provider = APIProvider(config['API_URL'],
                                config['API_KEY'],
                                config['API_KEY_QUERY_PARAM_KEYWORD'],
                                config['API_ROUTE'],
                                config['SEARCH_QUERY_PARAM_KEYWORD'],
                                config['SEARCH_KEYWORD'])

    mail_provider = Mailer(mail_config['MAIL_AUTH_EMAIL'],
                    mail_config['MAIL_AUTH_PASSWORD'],
                    mail_config['SMTP_SERVER'],
                    mail_config['SMTP_PORT'],
                    json.loads(mail_config['MAIL_RECEIVERS']))

    schedule.every(10).seconds.do(job, http_provider, mail_provider)


def _setup_logger():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    _setup_logger()
    setup_scheduler()
    write_timestamp_to_file(datetime.datetime.now())
    schedule_runner()

