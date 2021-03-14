from datetime import datetime


def datetime_from_reference(response):
    time_ = response['data']['plan']['paidAt']
    year = time_.split("-")[0]
    month = time_.split("-")[1]
    day = time_.split("-")[2]
    paid_at = datetime(year, month, day, 1, 1, 1)
    return paid_at
