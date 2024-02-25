from datetime import datetime
def drop():
    day = datetime.now().replace(microsecond=0)
    return day
print(drop())