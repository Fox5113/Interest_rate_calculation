from calendar import monthrange
from datetime import date, timedelta, datetime
import json


def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta


class Credit:
    def __init__(self, start_sum=0, start_date=date.today(),
                 end_date=date.today() + timedelta(35), rate=0.01,
                 start_perv=date.today(), end_perv=date.today() + timedelta(35)):
        self.start_sum = start_sum
        self.start_date = start_date
        self.end_date = end_date
        self.rate = rate
        self.start_perv = start_perv
        self.end_perv = end_perv

    def cal_monthly_payment(self):
        months = monthdelta(self.start_date, self.end_date)
        months_rate = self.rate / 12
        inter_paid = self.start_sum * months_rate
        return inter_paid / (1 - (1 + months_rate) ** (-months))

    def cal_total_perv(self):
        months = monthdelta(self.start_perv, self.end_perv)
        return self.cal_monthly_payment() * months

    def __str__(self):
        return " total_pay: " + str(self.cal_total_perv()) + "  "


'''
credit = {
        "start_sum": 15000,
        "start_date": str(date.today()),
        "end_date": str(date.today() + timedelta(365*5 + 3)),
        "rate": 0.04,
        "start_perv": str(date.today()),
        "end_perv": str(date.today() + timedelta(365*5 + 3))
    }
'''

with open('date.json') as f:
    atributes = json.load(f)
    start_sum = atributes['start_sum']
    start_date = datetime.strptime(atributes['start_date'], '%Y-%m-%d').date()
    end_date = datetime.strptime(atributes['end_date'], '%Y-%m-%d').date()
    rate = atributes['rate']
    start_perv = datetime.strptime(atributes['start_perv'], '%Y-%m-%d').date()
    end_perv = datetime.strptime(atributes['end_perv'], '%Y-%m-%d').date()
    credit = Credit(start_sum, start_date, end_date, float(rate), start_perv, end_perv)
    print(credit)
