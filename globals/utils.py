import datetime

current_month = datetime.datetime.now() - datetime.timedelta(days=30)
now = datetime.datetime.now()

"""
this for getting the last month
adding this condition is important because if we're in Jan 
and we do need to get the analytics of the last month will throw an error
"""
if now.month == 1:
    one_month_ago = datetime.datetime(now.year, 12, 1)
    one_month_ago_end = datetime.datetime(now.year, 12, 30)
else:
    one_month_ago = datetime.datetime(now.year, now.month - 1, 1)
    one_month_ago_end = datetime.datetime(now.year, now.month - 1, 30)

start_week = now.today() - datetime.timedelta(now.weekday())
end_week = start_week + datetime.timedelta(7)


def calculate_profits(sales, sales_count):
    profits = 0
    if sales_count == 0:
        profits = 0

    for sale in sales:
        print(sale.total)
        profits += sale.total

    return profits


def calculate_increase_percentage(current_count, past_count):
    if current_count == past_count:
        return 0
    if past_count == 0:
        return 100.0
    else:
        return (current_count - past_count) / past_count
