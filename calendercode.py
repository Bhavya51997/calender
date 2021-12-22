from datetime import date

import calendar

import time

import re

import sys

#for highlighting the calendar

def cal_highlight(newm,nyear):

    print("inside calhightlight",newm)

    if newm>0:

        thism = calendar.month(nyear, newm)  # current month

    else:

        year = today.year

        month = today.month

        thism = calendar.month(year, month)  # current month

    date = today.day.__str__().rjust(2)

    rday = ('\\b' + date + '\\b').replace('\\b ', '\\s')

    rdayc = "\033[7m" + date + "\033[0m"

    #             7 Swaps foreground and background colors

    print(re.sub(rday, rdayc, thism))

def cal_process():

    m = 0

    #input

    while(True):

        m = int(input("Enter the month between 1 - 12:"))

        if (m>=-12 & m<=12):

            if m > 0:

                # positive value

                sum = month + m

                if sum > 12:

                    newm = sum - 12

                    nyear = year + 1

                elif sum < 12:

                    newm = sum

                    nyear = today.year

                elif sum==12:

                    newm = month + 1

                    nyear = today.year

            elif m < 0:

                # negative value

                diff = month + m

                if diff < 0:

                    newm = diff + 12

                    nyear = year - 1

                elif diff > 0:

                    newm = diff

                    nyear = today.year

            elif m==0:

                newm = today.month

                nyear = today.year

            cal_highlight(newm,nyear)

            print(newm)

            ex=input("if you wish to exit press [YES/NO]: ")

            if ex=="NO":

                sys.exit()

        else:

            print("Months should be in between -12 and +12")

            sys.exit()

attempts=0

username="Bhavya"

password="bhavya123"

while(True):

    attempts+=1

    uname = input("Enter the username: ")

    pword = input("Enter the password: ")

    if ((uname == "Bhavya") & (pword == "bhavya123")):

        today = date.today()

        year = today.year

        month = today.month

        print(month)

        newm = 0

        nyear = 0

        cal_highlight(month,year)

        cal_process()

    if attempts>3:

        print("Sorry wrong username and password \n Your attempts are over")

        sys.exit()
