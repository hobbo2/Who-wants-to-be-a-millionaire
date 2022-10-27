### calculate how long it takes for you to become a millionaire by saving in
# 1 sp500: The average annualized return since adopting 500 stocks into the index in 1957 through Dec. 31, 2021, is 11.88%.
#
# 2 stocks
'''
formula for installments with compound interest: S = (P - P[1 + r / n ]**nt) / (1 - [1 + r / n])
to work out how many periods n x t need to use logs: top = 1 - S(1 - [1 + r / n]) / P
                                        There for Log(top) / Log(1 + r / n)
monthly contributions (p) = s - s (1 + i) / 1 + (1 + i)**mn
'''

import math
import sys
# Global variables

s = 1000000 # final amount
r = float(11.88/100) # convert s&p500 annual return to effective monthly rate
i = float(r / 12) # effective rate



def main():
    x = input('Do you want to:\n (A): calculate how long it will take to save your first million investing a fixed amount in the S&P500 monthly?\n OR \n (B): Calculate how much you should save in the S&P500 per month to reach 1 000 000 within your time period?\n Type A or B: ')

    letter = profile(x)
    result = option_check(letter)
    print(result)
    sys.exit()


 # do users want how long it will take or how much to save within a period
def profile(x):
    while True:
        try:
            letter = x.upper()
            if letter == 'A' or letter == 'B':
                return letter
            else:
                main()
        except ValueError:
            print('INVALID !  Please enter: A or B')

def option_check(f):
    if f == 'A':
        pay_periods, amount = option_a()
        years, months = time(pay_periods)
        result = f"It will take {years} years and {months} months investing {amount} in the S&P500 to reach 1000 000"
        return result
    if f == 'B':
        amount, time_frame = option_b()
        result = f'You will reach 1 000 000 in {time_frame} years by investing {amount} in the S&P500 Monthly'
        return result



def option_a():
    # error check for ints
    while True:
        try:
            # monthly amount
            p = int(input('How much do you plan on saving in the S&P500 per month?\n'))

            # calculate years
            top = 1 - (s * (1 - (1 + i)) / p)

            periods = math.log(top) / math.log(1 + i)

            return periods, p

        except ValueError:
            print('Enter valid number\n')

def time(x):
    years = math.floor(x / 12)
    months = math.floor(12 * (x / 12 - math.floor(years)))
    return years, months


def option_b():
    while True:
        try:
            time_frame = int(input('What time frame do you have to reached 1 000 000 in years?\n'))

            # calculationg p: the monthly payment needed
            periods = time_frame * 12
            top = s - s * (1 + i)
            bottom = 1 - (1 + i ) ** periods
            amount = round(top / bottom , 2)
            return amount, time_frame
        except ValueError:
            print('Please Enter VALID NUMBER...\n')



if __name__ == '__main__':
    main()
