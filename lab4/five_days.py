from datetime import datetime, timedelta
def five_days(days):
    current_date = datetime.now()
    subtracted_date = datetime.now() - timedelta(days=days)
    return subtracted_date

days = float(input())
print(five_days(days))
