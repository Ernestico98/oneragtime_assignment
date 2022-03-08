from .models import User, Bill, Investment
from datetime import datetime
from django.db.models import Sum
from datetime import date

def Membership(user_row):
    cur_year = datetime.today().year
    inversions = Investment.objects.all().filter(investment_date__year=cur_year, user=user_row).aggregate(Sum('investment_amount'))['investment_amount__sum']
    if inversions >= 50000:
        return 0
    return 3000

def up_front_fees(investment_row):
    if investment_row.up_front_payed == True:
        return 0
    return investment_row.fee_percentage * investment_row.investment_amount * 5

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def yearly_fees(investment_row):
    top = datetime.date(2019, 4, 1)
    ongoing_year = (date.today() - investment_row.investment_date) // 365 + 1
    if investment_row.investment_date < top:
        if ongoing_year == 1:
            return 365 * investment_row.fee_percentage * investment_row.invested_amount
        else:
            return investment_row.fee_percentage * investment_row.invested_amount
    else:
        if ongoing_year == 1:
            num = (investment_row.investment_date - date(investment_row.investment_date.year, 1, 1)).days + 1
            den = 365 + is_leap_year(investment_row.investment_date.year)
            return (num / den) * investment_row.fee_percentage * investment_row.invested_amount
        elif ongoing_year == 2:
            return investment_row.fee_percentage * investment_row.invested_amount
        elif ongoing_year == 3:
            return max(0, investment_row.fee_percentage - 0.2) * investment_row.invested_amount
        elif ongoing_year == 4:
            return max(0, investment_row.fee_percentage - 0.5) * investment_row.invested_amount 
        else:
            return max(0, investment_row.fee_percentage - 1.0) * investment_row.invested_amount 

        


