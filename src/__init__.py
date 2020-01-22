import configparser
import schedule
import time
import datetime


def job(config):
    datetime_instance = datetime.datetime.strptime('2019-01-04T16:41:24+0200', "%Y-%m-%dT%H:%M:%S%z")
    write_timestamp_to_file(datetime_instance)


def write_timestamp_to_file(datetime_instance):
    ts_file = open('../last_news_update', 'w')
    ts_file.write(datetime_instance.isoformat())
    ts_file.close()


def get_config():
    config_parser = configparser.RawConfigParser()
    config_parser.read('../config.cfg')
    return config_parser.items('DEFAULT')


def setup_scheduler():
    config = get_config()
    schedule.every(3).seconds.do(job, config)


def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    setup_scheduler()
    schedule_runner()
