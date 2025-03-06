
import datetime


def default_expiry_date():
    return (datetime.datetime.now() + datetime.timedelta(days=30)).date()
