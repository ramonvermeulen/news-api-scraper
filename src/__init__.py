import configparser
import schedule
import time
import datetime


def job(config):
    ts_file = open('../lastnews_datetime', 'w')
    timestamp = datetime.datetime.now().isoformat()
    ts_file.write(timestamp)
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
