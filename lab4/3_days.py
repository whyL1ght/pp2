from datetime import datetime, timedelta
def three_days():
    yesterday = datetime.now() - timedelta(days=1)
    today = datetime.now()
    tomorrow = datetime.now() + timedelta(days=1)
    return yesterday, today, tomorrow


print(three_days())
